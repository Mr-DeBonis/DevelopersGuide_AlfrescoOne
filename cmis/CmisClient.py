'''
 This program aims to get the same functionality as the one described
 in the book Alfresco One 5.x Developer's guide

 Author: Ignacio De Bonis
 Date:   19 October 2021
'''
import cmislib
import base64
from cmislib.model import CmisClient

# user credentials
userName = 'admin'
userPass = 'admin'

# connection settings
repositoryUrl = 'http://localhost:8080/alfresco/api/-default-/public/cmis/versions/1.1/atom'


def createDocument(session):
    # Create a Marketing folder with a text file that has relationship with a whitepaper
    # Locate document library
    path = '/Sites/marketing/documentLibrary'
    documentLibrary = session.getObjectByPath(path)

    # Locate the marketing folder
    marketingFolder = None
    for child in documentLibrary.getChildren():
        if child.name == 'Marketing':
            marketingFolder = child

    # create the marketing folder if needed
    if marketingFolder == None:
        marketingFolder = documentLibrary.createFolder('Marketing')

    # prepare properties
    filename = 'Mi documento3.txt'
    properties = {'cmis:name': filename,
                  'cmis:objectTypeId': 'D:sc:marketingDoc'}

    # prepare content
    content = 'Hola Mundo 4!'
    mimetype = 'text/plain; charset=UTF-8'

    marketingDocument = marketingFolder.createDocument(name=filename, properties=properties,
                                                       contentFile=str(base64.b64encode(
                                                           content.encode('UTF-8')))[2:-1],
                                                       contentType=mimetype, contentEncoding='UTF-8')

    # Locate the whitepaper folder
    whitepaperFolder = None
    for child in documentLibrary.getChildren():
        if child.name == 'Whitepapers':
            whitepaperFolder = child

    # look for a whitepaper
    if whitepaperFolder != None:
        whitepaper = None
        for child in whitepaperFolder.getChildren():
            if child.properties['cmis:objectTypeId'] == 'D:sc:whitepaper':
                whitepaper = child

        # Create relationship between marketingDocument and whitepaper
        if whitepaper != None:
            relationship = marketingDocument.createRelationship(
                whitepaper, 'R:sc:relatedDocuments')


def searchDocuments(session, maxItems=5):

    # Perform cmis query and print the result properties
    maxItems = str(maxItems)
    results = session.query("SELECT * FROM sc:doc", maxItems=maxItems)
    for hit in results:
        for prop in hit.properties:
            print(prop, ":", hit.properties[prop])
        print('--------------------------------------')

def deleteDocuments(session):
    # Delete all documents from the Marketing folder
    # Locate document library
    path = '/Sites/marketing/documentLibrary'
    documentLibrary = session.getObjectByPath(path)
    
    # Locate the marketing folder
    marketingFolder = None
    for child in documentLibrary.getChildren():
        if child.name == 'Marketing':
            marketingFolder = child

    # Delete documents in marketing folder
    if marketingFolder != None:
        for child in marketingFolder.getChildren():
            child.delete()   


#############################################################

try:

    # create session
    client = CmisClient(repositoryUrl, userName, userPass)
    repo = client.defaultRepository

    # createDocument(repo)
    searchDocuments(repo, 10)
    # deleteDocuments(repo)

except Exception as exception:
    print(type(exception).__name__)

