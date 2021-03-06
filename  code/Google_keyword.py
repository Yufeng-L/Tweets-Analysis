from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

document = language.types.Document(
    content='Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew".',
    type=language.enums.Document.Type.PLAIN_TEXT,
)
response = client.analyze_entities(
    document=document,
    encoding_type='UTF32',
)
for entity in response.entities:
    print('=' * 20)
    print('         name: {0}'.format(entity.name))
    print('         type: {0}'.format(entity.type))
    print('     metadata: {0}'.format(entity.metadata))
    print('     salience: {0}'.format(entity.salience))