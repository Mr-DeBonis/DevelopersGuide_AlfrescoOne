# DevelopersGuide_AlfrescoOne
Although this is my follow up of the examples from the book "[Alfresco One 5.x Developer's Guide](https://github.com/PacktPublishing/Alfresco-One-5x-Developers-Guide)", this development uses the **alfresco all-in-one SDK 3.1.0**, aiming for Alfresco 5.2.x customizations.

# Features

1. SDK settings
   - AMP packaging
   - debug-client mode set to false
2. Create custom models
   - Implement the someCo custom model
     - Add it to the UI
     - Add properties and types to advanced search
    - Working with content programatically
      - Create content with JavaScript using the *Manage rules* from a custom folder.
      - Create, search and delete content from cmislib3 ( Using cmis 1.1.0 instead of the outdated java cmis package v0.13.4)

# Test it out!
## Custom models
1. Create a *Marketing* Site, with a *Document Library*
2. Create a *Whitepapers* folder
   - Add the rule: when creating content, execute script *createWhitepaper.js*
3. Upload a document to the folder
4. Run the program from cmis directory. Uncomment each function and see how they work.