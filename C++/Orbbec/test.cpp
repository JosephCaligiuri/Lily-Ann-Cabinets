#include <OpenNI.h>
#include <iostream>

int main(int argc, char** argv)
{
    openni: :Status rc = openni: :STATUS_OK;

    // initialize OpenNI library
    rc = openni: :OpenNI: :initialize();
    if (rc != openni: :STATUS_OK)
    {
        std: :cerr << "Failed to initialize OpenNI" << std: :endl;
        return 1;
  }
  // open device
    openni: :Device device;
    rc = device.open(openni: :ANY_DEVICE);
    if (rc != openni: :STATUS_OK)
    {
        std: :cerr << "Failed to open device" << std: :endl;
        return 1;
  }
  // create depth stream
    openni: :VideoStream depthStream;
    rc = depthStream.create(device, openni: :SENSOR_DEPTH);
    if (rc == openni: :STATUS_OK)
    {
    // set video mode
        openni: :VideoMode depthMode;
        depthMode.setResolution(640,
    480);
        depthMode.setFps(30);
        depthMode.setPixelFormat(openni: :PIXEL_FORMAT_DEPTH_1_MM);
        depthStream.setVideoMode(depthMode);

        // start depth stream
        rc = depthStream.start();
        if (rc != openni: :STATUS_OK)
        {
            std: :cerr << "Failed to start depth stream" << std: :endl;
            depthStream.destroy();
            return 1;
    }
  }
    else
    {
        std: :cerr << "Failed to create depth stream" << std: :endl;
        return 1;
  }
  // create color stream
    openni: :VideoStream colorStream;
    rc = colorStream.create(device, openni: :SENSOR_COLOR);
    if (rc == openni: :STATUS_OK)
    {
    // set video mode
        openni: :VideoMode colorMode;
        colorMode.setResolution(640,
    480);
        colorMode.setFps(30);
        colorMode.setPixelFormat(openni: :PIXEL_FORMAT_RGB888);
        colorStream.setVideoMode(colorMode);

        // start color stream
        rc = colorStream.start();
        if (rc != openni: :STATUS_OK)
        {
            std: :cerr << "Failed to start color stream" << std: :endl;
            colorStream.destroy();
            return 1;
    }
  }
    else
    {
        std: :cerr << "Failed to create color stream" << std: :endl;
        return 1;
  }
  // main loop
    while (true)
    {
        openni: :VideoFrameRef depthFrame;
        openni: :VideoFrameRef colorFrame;

        // wait for new frames
        rc = openni: :OpenNI: :waitForAnyStream(&depthStream,
    1, NULL,
    2000);
        if (rc != openni: :STATUS_OK)
        {
            std: :cerr << "Failed to wait for depth frame" << std: :endl;
            return 1;
    }

        rc = openni: :OpenNI: :waitForAnyStream(&colorStream,
    1, NULL,
    2000);
        if (rc != openni: :STATUS_OK)
        {
            std: :cerr << "Failed to wait for color frame" << std: :endl;
            return 1;
    }
    // get depth frame
        rc = depthStream.readFrame(&depthFrame);
        if (rc != openni: :STATUS_OK)
        {
            std: :cerr << "Failed to read depth frame" << std: :endl
            continue;
                    // get color frame
        rc = colorStream.readFrame(&colorFrame);
        if (rc != openni: :STATUS_OK)
        {
            std: :cerr << "Failed to read color frame" << std: :endl;
            continue;
      }
      // convert depth frame to 16-bit grayscale
        cv: :Mat depthImage;
        if (depthFrame.getVideoMode().getPixelFormat() == openni: :PIXEL_FORMAT_DEPTH_1_MM)
        {
            depthImage = cv: :Mat(depthFrame.getHeight(), depthFrame.getWidth(), CV_16UC1, (void*)depthFrame.getData());
      }
        else
        {
            openni: :VideoFrameRef convertedDepthFrame;
            rc = depthFrame.convertTo(convertedDepthFrame, openni: :PIXEL_FORMAT_DEPTH_1_MM);
            if (rc != openni: :STATUS_OK)
            {
                std: :cerr << "Failed to convert depth frame" << std: :endl;
                continue;
        }
            depthImage = cv: :Mat(convertedDepthFrame.getHeight(), convertedDepthFrame.getWidth(), CV_16UC1, (void*)convertedDepthFrame.getData());
      }
      // convert color frame to OpenCV Mat
        cv: :Mat colorImage(colorFrame.getHeight(), colorFrame.getWidth(), CV_8UC3, (void*)colorFrame.getData());

        // do something with the frames
      // ...
      // display frames
        cv: :imshow("depth", depthImage);
        cv: :imshow("color", colorImage);
        cv: :waitKey(1);
    }
    // destroy streams and shutdown OpenNI
    depthStream.destroy();
    colorStream.destroy();
    openni: :OpenNI: :shutdown();

    return 0;
  }