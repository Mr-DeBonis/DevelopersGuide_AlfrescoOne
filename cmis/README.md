# CmisClient.py
To use this program, there should be a site called "Marketing" with a Document Library containing a "Whitepapers" folder and some files of type sc:whitepaper in it.

## createDocument()
Creates a "Marketing" folder in the Document Library if there is none. Then, it creates a txt file in it with associated to the file in the "Whitepapers" folder.

## searchDocument()
Makes a cmis query for all the documents with sc:doc type.

## deleteDocuments()
Search for the "Marketing" folder in the document library and if there is one, this function deletes it.
