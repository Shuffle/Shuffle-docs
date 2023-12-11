# Enrichment
The goal of enrichment is to add more information to an existing usecase. It should typically be done for each alert or incident found, and have a standardized output.

## Input
The input should be sent into a Subflow. The basic process goes like this:

0. Start from a Schedule
1. Get tickets/alerts
2. Deduplicate them
3. **Send each ticket for enrichment**
4. Send further

We focus on step 3 in this part - the subflow itself.

## Subflow
Build the general enrichment subflow to do the following: 

1. Find different IOC types
2. **Send each IOC type to another subflow**
3. Get each IOC type back
4. Standardize the output (remember to set Default Output in the Edit Workflow section)

**Input:**
```
Anything
```

**Output:**
```
{
  "message": "Malicious domain found!",
  "indicators": [{
    "type": "ip",
    "value": "1.2.3.4",
    "malicious": false
  },
  {
    "type": "domain",
    "value": "malicious.com",
    "malicious": true,
    "confidence": "0.9"
  }]
}
```

The indicators should come from a subflow for each type. See next section

## Sub-Subflow (handle each type)
Build the specific enrichment sub-subflow to do the following:

1. Get the IOC type
2. Search YOUR Intel for it
3. Format the data to be standardized one (with default output)


**Input:**
```
Anything
```

**Output:**
```
{
  "message": "Malicious domains found!",
  "type": "domain",
  "indicators": [
  {
    "type": "domain",
    "value": "malicious.com",
    "malicious": true,
    "confidence": "0.9"
  }]
}
```

The output of this is sent to the parent workflow.

# Conclusion
The subflow here should be standardized for ANY data and work for ANYTHING. Our guidelines for output are GUIDELINES. The point is to 
work on standardization to make sure we can analyze data from ANY intel tool the same way, and make it easy to swap between them.

If you need help with this, contact support@shuffler.io
