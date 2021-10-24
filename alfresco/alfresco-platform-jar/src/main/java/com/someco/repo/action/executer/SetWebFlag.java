package com.someco.repo.action.executer;

import java.io.Serializable;
import java.util.Date;
import java.util.List;
import java.util.Map;

import com.someco.repo.common.SomeCoModel;

import org.alfresco.repo.action.ParameterDefinitionImpl;
import org.alfresco.repo.action.executer.ActionExecuterAbstractBase;
import org.alfresco.service.cmr.action.Action;
import org.alfresco.service.cmr.action.ParameterDefinition;
import org.alfresco.service.cmr.dictionary.DataTypeDefinition;
import org.alfresco.service.cmr.repository.NodeRef;
import org.alfresco.service.cmr.repository.NodeService;
import org.alfresco.service.namespace.QName;

public class SetWebFlag extends ActionExecuterAbstractBase {
    protected NodeService nodeService;
    public final static String NAME = "set-web-flag";
    public final static String PARAM_ACTIVE = "active";

    @Override
    protected void executeImpl(Action action, NodeRef actionedUponNodeRef) {
        // Set isActive to true if null
        boolean activeFlag = true;
        if (action.getParameterValue(PARAM_ACTIVE) != null){
            activeFlag = (Boolean) action.getParameterValue(PARAM_ACTIVE);
        }

        // Grab current properties from the node and add it to the map
        Map<QName, Serializable> properties = nodeService.getProperties(actionedUponNodeRef);
        properties.put(SomeCoModel.PROP_ISACTIVE, activeFlag);

        // Set published date to the current date
        if (activeFlag) {
            properties.put(SomeCoModel.PROP_PUBLISHED, new Date());
        }

        // if the aspect has already been added, set the properties
        if (nodeService.hasAspect(actionedUponNodeRef, SomeCoModel.ASPECT_WEBABLE)) {
            nodeService.setProperties(actionedUponNodeRef, properties);
        } else {
            nodeService.addAspect(actionedUponNodeRef, SomeCoModel.ASPECT_WEBABLE, properties);
        }
    }

    @Override
    protected void addParameterDefinitions(List<ParameterDefinition> paramList) {
        // This method defines the parameters for the action
        paramList.add(new ParameterDefinitionImpl(PARAM_ACTIVE, 
                                                  DataTypeDefinition.BOOLEAN, 
                                                  false,
                                                  getParamDisplayLabel(PARAM_ACTIVE)));
    }
    

    //Param nodeService to set
    public void setNodeService(NodeService nodeService) {
		this.nodeService = nodeService;
	}
}
