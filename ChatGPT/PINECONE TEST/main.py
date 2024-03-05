import pinecone

pinecone.init(api_key="fb19b80f-cf23-4e4e-83ac-b8114b2b0993", environment="asia-southeast1-gcp-free")

index = pinecone.Index("quickstart")

upsert_response = index.upsert(
    vectors=[
        {'id': 'vec1',
         'values': [0.1, 0.2, 0.3],
         'metadata': {'genre': 'drama'},
         'sparse_values': {
             'indices': [10, 45, 16],
             'values': [0.5, 0.5, 0.2]
         }},
        {'id': 'vec2',
         'values': [0.2, 0.3, 0.4],
         'metadata': {'genre': 'action'},
         'sparse_values': {
             'indices': [15, 40, 11],
             'values': [0.4, 0.5, 0.2]
         }}
    ],
    namespace='example-namespace'
)

