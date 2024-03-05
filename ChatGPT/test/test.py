from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define your training data as input-output pairs
training_data = [
{"prompt":"What are builder grade cabinets?","completion":" Builder-grade, or contractor-grade, is an industry term for a product built to meet construction code requirements, using simple, inexpensive materials with minimal detailing.\n"},
{"prompt":"What type of wood are your cabinets made from?","completion":" The box is constructed of a 7 ply plywood, face frame is a birch wood and the doors are HDF (High Density Fiberboard).\n"},
{"prompt":"Are the cabinets made from Plywood?","completion":" The box is constructed of a 7 ply plywood, but the face frame is a birch wood and the doors are HDF (High Density Fiberboard).\n"},
{"prompt":"What is HDF?","completion":" HDF stands for high-density fiberboard, it is a type of fiberboard, which is an engineered wood product.\n"},
{"prompt":"What is SPC flooring?","completion":" SPC flooring is luxury vinyl plank or tile flooring with a stone-plastic composite core. Also known as rigid core or engineered vinyl flooring, it's manufactured in four or five layers, depending on whether the backing is foam or cork. The backing is often added for comfort and insulation. While laminate generally also has four layers, the core materials are different. SPC flooring is generally more durable.\n"},
{"prompt":"How does SPC flooring compare to laminate or vinyl?","completion":" A vinyl floor has a simple PVC core that makes it flexible and soft. The SPC vinyl planks have a core made of a stone plastic composite, which gives it a rigid construction. While laminate also has layers, pressed wood boards with a repeating printed image of wood fused onto a fiberboard core. SPC flooring is generally more durable.\n"},
{"prompt":"Can you modify the depth of cabinets?","completion":" Yes! Lily Ann Cabinets can make modifications to your cabinets such as changing the depths of the cabinetry to best fit your space!\n"},
{"prompt":"Are Lily Ann Cabinets custom made?","completion":" Our cabinets are RTA cabinets (Ready-to-assemble), but we do offer customization of our cabinets for a small fee.\n"},
{"prompt":"Are Lily Ann Cabinets premium cabinets?","completion":" Yes, Lily Ann Cabinets is premium cabinetry with the lowest prices on the market today.\n"},
{"prompt":"Do you offer delivery?","completion":" Yes! If you are in Michigan, Ohio, or Florida, Lily Ann Cabinets will be delivering your cabinets on their very own trucks! Since the cabinets never leave Lily Ann until they are with you, there is less room for damages to occur during delivery. The Lily Ann drivers will also bring your cabinets to whatever room you would like them instead of just leaving them at the curb.\n"},
{"prompt":"Where are you located?","completion":" Lily Ann Cabinets has two warehouses located in Largo Florida and Adrian Michigan and showrooms in Temperance MI, Adrian, MI and Largo, FL. Our headquarters is our Adrian warehouse.\n"},
{"prompt":"Does Lily Ann Cabinets do installation?","completion":" We do installation of our custom granite countertops, but unfortunately Lily Ann Cabinets only provides the cabinets. However, you can always give us a call, watch our online videos, use our interactive assembly instructions through the bilt app, or video chat with a professional through the Lily Ann Cabinets App if you have any questions or need any help! If you are not looking to install the cabinets yourself, we recommended hiring a contractor in your area.\n"},
{"prompt":"Do you offer kitchen designs?","completion":" Yes! Lily Ann Cabinets has a team of professional designers ready to design your dream space! All designs done at Lily Ann Cabinets are free of charge and are emailed to you within 24 hours. You can make as many changes to the design you would like and will also receive a quote with it.\n"},
{"prompt":"Do you offer bathroom designs?","completion":" Yes! Lily Ann Cabinets can provide cabinetry for any space in your home such as kitchens, bathrooms, mudrooms, laundry rooms, bars, offices, garages, etc.\n"},
{"prompt":"How long, after I place my order, will it take until I receive it?","completion":" Lily Ann Cabinets ship out in three days, so you could have your cabinetry at your doorstep within days of placing your order! Lily Ann Cabinets can also push or slow your order depending on what best fits your needs!\n"},
{"prompt":"How long does shipping take?","completion":" Lily Ann Cabinets ship out in three days, so you could have your cabinetry at your doorstep within days of placing your order, but the actual time depends on where you’re located.\n"},
{"prompt":"How long do your cabinets last for?","completion":" Yes, they are designed and manufactured to last a lifetime.\n"},
{"prompt":"How does Lily Ann Cabinets ship their products?","completion":" Freight or by our own delivery trucks.\n"},
{"prompt":"Are your cabinets hand painted?","completion":" Doors and face frames are painted by hand and the box is machine painted.\n"},
{"prompt":"Does Lily Ann Cabinets have any social media accounts?","completion":" Yes! Our tiktok handle is: Lily.Ann.Cabinets, our pinterest is Lilyanncabinets, and our Youtube can be found by the name Lily Ann Cabinets.\n"},
{"prompt":"Does Lily Ann Cabinets have an app?","completion":" Yes, we do have an app!\n"},
{"prompt":"Can you modify a lazy susan cabinet?","completion":" You may modify a Lazy Susan but only decreasing the depth.\n"},
{"prompt":"What is the most popular style of cabinet?","completion":" Our most popular style is the White Shaker!\n"},
{"prompt":"What is the most popular color of cabinet?","completion":" Our most popular color of cabinet is white, like our best selling line, our White Shaker.\n"},
{"prompt":"What are the most popular color combinations for two-tone kitchens?","completion":" White\/Blue, Linen\/Saddle, and White\/Grey.\n"},
{"prompt":"What hardware is the most popular?","completion":" With white cabinets black long handles are very popular. With gray cabinets, silver handles are more popular.\n"},
{"prompt":"What are Lily Ann Cabinets’ best selling cabinet inserts?","completion":" Trash Pullouts, silverware and cutlery inserts. Lazy Susan turntables. Don’t forget our drip trays for your sink base.\n"},
{"prompt":"What is Lily Ann Cabinets’ best selling flooring?","completion":" Our SPC Flooring is our best selling flooring.\n"},
{"prompt":"What is Lily Ann Cabinets’ best selling backsplash?","completion":" Yes we do, They are shown on our website.\n"},
{"prompt":"What does Lily Ann Cabinets sell, other than cabinets?","completion":" We have flooring, cabinet organizers, handles, backsplashes, tiles, and much more!\n"},
{"prompt":"Does Lily Ann Cabinets sell countertops?","completion":" Yes, we sell custom made granite\/quartz countertops, but only within 2-3 hours radius of our Adrian, Michigan location.\n"},
{"prompt":"Does Lily Ann Cabinets make custom countertops?","completion":" Yes, we sell custom granite\/quartz countertops, but only within 2-3 hours radius of our Adrian, Michigan location.\n"},
{"prompt":"Do you sell backsplashes?","completion":" Yes! Our best selling backsplash is the subway tile.\n"},
{"prompt":"Does Lily Ann Cabinets sell flooring?","completion":" Yes, We offer four different styles of SPC flooring and tile.\n"},
{"prompt":"Does Lily Ann Cabinets sell toilets?","completion":" Yes, we sell many bathroom essentials at Lily Ann Cabinets!\n"},
{"prompt":"Does Lily Ann Cabinets offer builder grade cabinets?","completion":" Lily Ann Cabinets offers three builder grade cabinets: The Summit White Shaker, Madison Toffee, and Madison Chocolate. These Cabinets do not have the self-closing features like the premium cabinets do, which makes them less expensive.\n"},
{"prompt":"Do you sell sinks?","completion":" Yes we do, They are shown on our website.\n"},
{"prompt":"Do you sell range hoods?","completion":" Yes we do, They are shown on our website.\n"},
{"prompt":"Do you offer self\/soft close cabinets?","completion":" Yes, our cabinets have 6 way adjustable hinges, except our builder grade cabinets.\n"},
{"prompt":"Do you carry soft-close hinges?","completion":" Yes, our cabinets come standard with 6 way adjustable hinges, except the builder grade.\n"},


    
    # Add more training examples as needed
]

# Fine-tune the GPT model using your training data
def fine_tune_model(training_data):
    # Prepare the training examples in OpenAI Chat format
    examples = []
    for example in training_data:
        examples.append({'role': 'system', 'content': 'You are a helpful assistant that provides information About the company, Lily Ann Cabinets. you also work for this company and you answer in character.'})
        examples.append({'role': 'user', 'content': example['prompt']})
        examples.append({'role': 'assistant', 'content': example['completion']})

    # Fine-tune the GPT model with the training examples
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=examples,
        max_tokens=500,
        n=1,
        temperature=0.7,
        stop=None,
        user="You are a helpful assistant that provides information About the company, Lily Ann Cabinets. you also work for this company and you answer in character."
    )

    return response

# Interact with the trained chatbot
def interact_with_chatbot(conversation):
    last_4_messages = conversation[-4:]

    # Prepare the messages for chatbot interaction
    messages = [{'role': 'system', 'content': 'You are a helpful assistant that provides information about the company, Lily Ann Cabinets. You also work for this company and answer in character.'}]
    messages.extend(last_4_messages)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        n=1,
        temperature=0.7,
        stop=None,
    )

    return response.choices[0].message.content

conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['user_input']

    # Add user input to conversation history
    conversation_history.append({'role': 'user', 'content': user_input})

    # Generate chatbot response
    response = interact_with_chatbot(conversation_history)

    # Add chatbot response to conversation history
    conversation_history.append({'role': 'assistant', 'content': response})

    return jsonify({'response': response})


if __name__ == '__main__':
    # Fine-tune the model
    fine_tune_model(training_data)
    app.run(host="10.0.1.100", port="8500")