/*
Upload this script to Data dictionary/scripts in alfresco share.
You can call it from folder rules under the action "execute a script"

This will rename the document, change its properties and add
the sc:webable aspect.

Author: Ignacio De Bonis
Created: 14/10/2021
*/

// The document variable is a root object availabel when executed against a document
var contentType = "whitepaper";
var contentName = "wp-";
var timestamp = new Date().getTime();
var extension = document.name.substr(document.name.lastIndexOf(".") + 1);

// Specialize document type
document.specializeType("sc:" + contentType);
// Add sc:webable aspect (can be used without calling save)
document.addAspect("sc:webable");

//Set some properties
document.properties["cm:name"] = contentName + " (" + timestamp + ")." + extension;
document.properties["sc:isActive"] = true;
document.properties["sc:published"] = new Date("07/31/2016");

// Save the document 
document.save();
