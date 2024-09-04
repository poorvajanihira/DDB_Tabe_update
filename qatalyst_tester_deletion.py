import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')  # Replace 'us-west-2' with your desired region

# Specify your DynamoDB table name
table_name = 'qatalyst-tester-details'

# Get the DynamoDB table
table = dynamodb.Table(table_name)

# Specify the study_id for which you want to update tester_ids
study_id = 'fc86288d-9e82-440f-82fa-46720626bcde'  # Replace with your actual study_id

# List of tester_ids to update
tester_ids_to_update = [
    '02308bdb-24f5-4780-9157-aec0aa8821a2',
'0383b309-d001-443c-9e54-1ba6a2333cd5',
'061a166f-4bd8-4010-b7b5-7e8da111cf01',
'07221b9c-7bfd-439a-b435-a7f68f439b73',
'0eb46135-0df0-49e6-84d8-09abbb11c362',
'14991d30-42e6-41a4-bad6-6260fd6e028a',
'1a2d512e-ce6c-45f6-ada8-0191bea9c096',
'1dc35f2d-bff2-4e53-abef-54bc670adea4',
'2345585a-0a22-4626-baec-6c546fe18d89',
'23fbabf2-d713-4174-85c8-fe41c10627e2',
'24894f35-f41f-4982-b747-bbdc0a94bc86',
'272c0e31-427b-413e-a37b-07bcd23477d5',
'2cb54eb6-7e8c-4eb7-b844-58e90014ce55',
'2e7741f4-13e0-4eda-88c2-6c471da6fce9',
'393f9c5b-ef5d-4003-ac36-8195bed47aac',
'3b3436b8-6d20-4e42-828a-f4ae6698b60d',
'3b405678-d0df-4c2f-b071-a7654879f176',
'40dc7aa6-d62a-40bb-ac9f-4958fd42db78',
'49106839-3106-4b57-a9b2-a7e6887d53d0',
'4e7a342c-0c48-4094-bd5b-9ebbe16b21dd',
'4ed19e73-d8f0-481e-8ada-b87141ca9a71',
'4f1434d6-5794-463a-8e4e-26c874a916d9',
'4f1e80b5-b6e8-43f1-b487-abbbac5480b5',
'4f609796-d0ae-40d5-8643-9a08a01df721',
'54db0c4b-9363-4b0c-85d3-4bd7408b5d3c',
'55a5395a-975b-440b-975b-44dfb6552ff0',
'56ada3b4-353e-42de-b291-be76a866b9b9',
'5c805415-5b21-40bf-a65c-c26a61cde70d',
'5cf6b720-f28e-4d9b-bc17-fcbab64a44af',
'6019262f-50b9-428f-a44d-84fe39aa8f6e',
'64c1ef09-a297-4df7-acd2-ba8e454b0e9a',
'664fc6a8-3004-47af-b323-6e4527710f74',
'698b2951-15e0-4281-94dc-1cb920abbae7',
'6990b4ae-b704-4ed4-bd36-11bfb662e717',
'6e3ac28b-c2e4-4ab7-81c3-13cc167720e5',
'6e702553-efde-4f04-a3e7-b28cb8501d37',
'7fd29d3f-0a22-4c05-b8d4-3b974932b003',
'80b16ba7-8590-4913-9ebc-46b43c8882be',
'86fc03bc-0182-4e60-a63c-b80ecfadf11a',
'90d6f22d-1132-4b5e-8a98-c97aaa48c289',
'95536ce7-9874-4258-9f56-d6b2a14bfcc9',
'a044ac56-1ba3-4bdc-af02-c14f2154b6f9',
'a7c8ff7c-eef5-4801-a27d-60ce9569e8ba',
'aa5401d0-ae16-422f-96a1-188eb2d4d9cd',
'b3bb40a5-63b5-4b4e-b1ad-263d6d9457b8',
'b4c99bed-2d02-4022-9e3e-eba6a3fb7a2a',
'b7215eb4-018a-44dd-b8ff-905d2913c4e1',
'ba165481-b5cf-47c3-a0ee-a748f92bf176',
'bba4aedc-3406-49d6-901a-fec9cf87273f',
'bedc30cc-de81-4161-bafe-90a335944668',
'bee9897a-19ab-4ef7-861f-a786262703c3',
'c30d9778-6cb3-465a-b5f5-36ae720478a0',
'c4bc38c2-de89-46e7-8862-9796ac914562',
'c865eeb6-9964-4f55-aa80-aef54c3b261e',
'c8bda0a3-238c-4f85-83b8-e9c5b4ead466',
'cf64f1b5-b8f1-4bc9-ae23-51588a82499a',
'd04b96b3-a439-482a-a8d1-62878ae1e6dd',
'd9b1eb88-7009-4d60-abb3-029f88bd3108',
'f4c5e23a-b8ec-4cae-a5c1-27438806ccc3',
'ffc9a457-9355-47f2-bbc7-d74c64782c80',
    # Add more tester_ids as needed
]

# Update the preview attribute to True for the specified tester_ids
for tester_id in tester_ids_to_update:
    response = table.update_item(
        Key={
            'study_id': study_id,
            'tester_id': tester_id
        },
        UpdateExpression="SET preview = :val",
        ExpressionAttributeValues={
            ':val': True
        },
        ReturnValues="UPDATED_NEW"
    )
    print(f"Updated tester_id {tester_id} in study_id {study_id} with response: {response}")

print("Batch update completed!")
