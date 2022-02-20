import boto3
import botocore
import paramiko
from os.path import expanduser
from time import sleep

# this will create dynamodb resource object and
# here dynamodb is resource name
s = boto3.Session(
    region_name='us-east-1')
client = s.resource('dynamodb')
# this will search for dynamoDB table 
# your table name may be different
table = client.Table("users")
print(table.table_status)

table.put_item(Item= {'userid': '34','company':  'microsoft','dahdah':321})
table.put_item(Item= {'userid': '35','company':  'microsoft','fcuk':321})
x = table.get_item(Key={'userid':'35'})
print(x)
print(x['Item'])
'''
s = boto3.Session(
    region_name='us-east-1')
client = s.resource('dynamodb')
print(dir(client))
client.create_table(AttributeDefinitions='',
TableName='',
KeySchema=''
)
print(client.tables)
print(client.tables.all())
print(dir(client.tables.all()))
#client = boto3.client('dynamodb')
response = client.put_item(
    TableName='users',
    Item={
    	'S': 'suckmyass'
    }
    #     'string': {
    #         'S': 'string',
    #         'N': 'string',
    #         'B': b'bytes',
    #         'SS': [
    #             'string',
    #         ],
    #         'NS': [
    #             'string',
    #         ],
    #         'BS': [
    #             b'bytes',
    #         ],
    #         'M': {
    #             'string': {'... recursive ...'}
    #         },
    #         'L': [
    #             {'... recursive ...'},
    #         ],
    #         'NULL': True|False,
    #         'BOOL': True|False
    #     }
    # },
    # Expected={
    #     'string': {
    #         'Value': {
    #             'S': 'string',
    #             'N': 'string',
    #             'B': b'bytes',
    #             'SS': [
    #                 'string',
    #             ],
    #             'NS': [
    #                 'string',
    #             ],
    #             'BS': [
    #                 b'bytes',
    #             ],
    #             'M': {
    #                 'string': {'... recursive ...'}
    #             },
    #             'L': [
    #                 {'... recursive ...'},
    #             ],
    #             'NULL': True|False,
    #             'BOOL': True|False
    #         },
    #         'Exists': True|False,
    #         'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH',
    #         'AttributeValueList': [
    #             {
    #                 'S': 'string',
    #                 'N': 'string',
    #                 'B': b'bytes',
    #                 'SS': [
    #                     'string',
    #                 ],
    #                 'NS': [
    #                     'string',
    #                 ],
    #                 'BS': [
    #                     b'bytes',
    #                 ],
    #                 'M': {
    #                     'string': {'... recursive ...'}
    #                 },
    #                 'L': [
    #                     {'... recursive ...'},
    #                 ],
    #                 'NULL': True|False,
    #                 'BOOL': True|False
    #             },
    #         ]
    #     }
    # },
    # ReturnValues='NONE'|'ALL_OLD'|'UPDATED_OLD'|'ALL_NEW'|'UPDATED_NEW',
    # ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
    # ReturnItemCollectionMetrics='SIZE'|'NONE',
    # ConditionalOperator='AND'|'OR',
    # ConditionExpression='string',
    # ExpressionAttributeNames={
    #     'string': 'string'
    # },
    # ExpressionAttributeValues={
    #     'string': {
    #         'S': 'string',
    #         'N': 'string',
    #         'B': b'bytes',
    #         'SS': [
    #             'string',
    #         ],
    #         'NS': [
    #             'string',
    #         ],
    #         'BS': [
    #             b'bytes',
    #         ],
    #         'M': {
    #             'string': {'... recursive ...'}
    #         },
    #         'L': [
    #             {'... recursive ...'},
    #         ],
    #         'NULL': True|False,
    #         'BOOL': True|False
    #     }
    # }
)
response = client.query(
    TableName='string',
    IndexName='string',
    Select='ALL_ATTRIBUTES'|'ALL_PROJECTED_ATTRIBUTES'|'SPECIFIC_ATTRIBUTES'|'COUNT',
    AttributesToGet=[
        'string',
    ],
    Limit=123,
    ConsistentRead=True|False,
    KeyConditions={
        'string': {
            'AttributeValueList': [
                {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
            ],
            'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
        }
    },
    QueryFilter={
        'string': {
            'AttributeValueList': [
                {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
            ],
            'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
        }
    },
    ConditionalOperator='AND'|'OR',
    ScanIndexForward=True|False,
    ExclusiveStartKey={
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
    ProjectionExpression='string',
    FilterExpression='string',
    KeyConditionExpression='string',
    ExpressionAttributeNames={
        'string': 'string'
    },
    ExpressionAttributeValues={
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    }
)
'''