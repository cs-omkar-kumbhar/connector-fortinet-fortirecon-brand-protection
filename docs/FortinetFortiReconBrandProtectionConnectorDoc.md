## About the connector
FortiRecon is a Digital Risk Protection Service (DRPS) product that provides an outside-the-network view to the risks posed to your enterprise.
<p>This document provides information about the Fortinet FortiRecon Brand Protection Connector, which facilitates automated interactions, with a Fortinet FortiRecon Brand Protection server using FortiSOAR&trade; playbooks. Add the Fortinet FortiRecon Brand Protection Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Fortinet FortiRecon Brand Protection.</p>

### Version information

Connector Version: 2.1.0

FortiSOAR&trade; Version Tested on: 7.6.0-5012

Fortinet FortiRecon Brand Protection Version Tested on: v24.4.b

Authored By: Fortinet

Certified: Yes

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-fortinet-fortirecon-brand-protection</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Fortinet FortiRecon Brand Protection server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Fortinet FortiRecon Brand Protection server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Fortinet FortiRecon Brand Protection</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Server name or IP address to which you will connect and perform the automated operations
</td>
</tr><tr><td>API Key</td><td>API key to access the endpoint to which you will connect and perform the automated operations
</td>
</tr><tr><td>Organization ID</td><td>The organization ID on which FortiRecon operations are to be performed.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Code Repo Exposures</td><td>Retrieves a list of code repo exposures based on the filter criteria that you have specified.</td><td>get_code_repo_exposures <br/>Investigation</td></tr>
<tr><td>Get Code Repositories</td><td>Retrieves a list of code repository based on the filter criteria that you have specified.</td><td>get_code_repos <br/>Investigation</td></tr>
<tr><td>Get Code Repos Statistics</td><td>Retrieves statistics for code repos.</td><td>get_code_repos_stats <br/>Investigation</td></tr>
<tr><td>Get Code Repo Matched Domains Statistics</td><td>Retrieves statistics of matched domains for the Code Repo exposures based on the page number and the page size specified.</td><td>get_code_repo_matched_domains_stats <br/>Investigation</td></tr>
<tr><td>Get Domain Threats</td><td>Retrieves list of code domain threats based on the filter criteria that you have specified.</td><td>get_domain_threats <br/>Investigation</td></tr>
<tr><td>Get Domain Threats By ID</td><td>Retrieves details of threats on a domain based on the threat ID that you have specified.</td><td>get_domain_threats_by_id <br/>Investigation</td></tr>
<tr><td>Get Executive Exposures</td><td>Retrieves list of executive exposures based on the filter criteria that you have specified.</td><td>get_executive_exposures <br/>Investigation</td></tr>
<tr><td>Get Executive Profiles</td><td>Retrieves list of executive profiles based on the name of the executive, page number, and page size that you have specified.</td><td>get_executive_profiles <br/>Investigation</td></tr>
<tr><td>Get Open Bucket Exposures</td><td>Retrieves list of open bucket exposures based on the filter criteria that you have specified.</td><td>get_open_bucket_exposures <br/>Investigation</td></tr>
<tr><td>Get Rogue Apps</td><td>Retrieves a list of Rogue Apps based on the status and keywords that you have specified for the query; rogue apps are mobile applications trying to look like apps from trusted brands.</td><td>get_rogue_apps <br/>Investigation</td></tr>
<tr><td>Get Rogue App By ID</td><td>Retrieves details of a rogue app based on the Rogue App ID that you have specified.</td><td>get_rogue_app_by_id <br/>Investigation</td></tr>
<tr><td>Get Social Media Threats</td><td>Retrieves list of social media threats based on the filter criteria that you have specified.</td><td>get_social_media_threats <br/>Investigation</td></tr>
<tr><td>Get Domain Threats Statistics</td><td>Retrieves statistics for domain threats.</td><td>get_domain_threats_stats <br/>Investigation</td></tr>
<tr><td>Get Original Domains Statistics</td><td>Retrieves the statistics of original domains threats based on the page number and the page size specified.</td><td>get_original_domains_stats <br/>Investigation</td></tr>
<tr><td>Get Open Bucket Exposures Statistics</td><td>Retrieves the statistics of open bucket exposures.</td><td>get_open_bucket_exposures_stats <br/>Investigation</td></tr>
<tr><td>Get Social Media Threats Statistics</td><td>Retrieves the statistics of social media threats.</td><td>get_social_media_threats_stats <br/>Investigation</td></tr>
<tr><td>Get Tags</td><td>Retrieves the list of active tags.</td><td>get_tags <br/>Investigation</td></tr>
<tr><td>Get Takedown Requests</td><td>Retrieves a list of takedown requests for rogue apps and typo domains for the given organization the filter criteria that you have specified.</td><td>get_takedown_requests <br/>Investigation</td></tr>
<tr><td>Update Code Repo Status</td><td>Updates the status of the Code Repo record.</td><td>update_code_repo_status <br/>Investigation</td></tr>
<tr><td>Update Domain Threat Status</td><td>Updates the status of the Domain Threat record.</td><td>update_domain_threat_status <br/>Investigation</td></tr>
<tr><td>Update Open Bucket Exposure Status</td><td>Updates the status of the Open Bucket Exposure record.</td><td>update_open_bucket_exposure_status <br/>Investigation</td></tr>
<tr><td>Update Rogue App Status</td><td>Updates the status of the Rogue App record.</td><td>update_rogue_app_exposure_status <br/>Investigation</td></tr>
<tr><td>Update Social Media Threat Status</td><td>Updates the status of the Social Media Threat record.</td><td>update_social_media_threat_status <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Code Repo Exposures
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search By Keyword</td><td>(Optional) Specify a keyword to search in code repo exposures and retrieve results containing the specified keyword.
</td></tr><tr><td>Matched Domain</td><td>(Optional) Specify a domain to search in code repo exposures and retrieve results containing the specified domain name. You can specify multiple comma-separated domains to retrieve code repo exposures containing the specified domains. For example: domain1.com,domain2.com.
</td></tr><tr><td>Risk Level</td><td>(Optional) Specify a risk level to search in code repo exposures and retrieve results containing the specified risk level. You can specify multiple comma-separated risk levels to retrieve code repo exposures containing the specified risk levels. For example, LOW,MEDIUM,HIGH.
</td></tr><tr><td>Attribute Type</td><td>(Optional) Specify an attribute type to search in code repo exposures and retrieve results containing the specified attribute type. You can specify multiple comma-separated attribute types to retrieve code repo exposures containing the specified attribute types. For example, Email,Password.
</td></tr><tr><td>Status</td><td>(Optional) Select a status to search in code repo exposures and retrieve results containing the specified status. You can select from following options: Active Ignored Resolved
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when a profile was added. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when a profile was added. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "added_ts": "",
            "attribute": "",
            "attribute_type": "",
            "id": "",
            "matched_domain": "",
            "raw_info": "",
            "risk_level": "",
            "status": "",
            "url": "",
            "repo_id": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Code Repositories
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search By Keyword</td><td>(Optional) Specify a keyword to search in code repositories and retrieve results containing the specified keyword.
</td></tr><tr><td>Matched Domain</td><td>(Optional) Specify a domain to search in code repositories and retrieve results containing the specified domain name. You can specify multiple comma-separated domains to retrieve code repo exposures containing the specified domains. For example: domain1.com,domain2.com.
</td></tr><tr><td>Risk Level</td><td>(Optional) Specify a risk level to search in code repositories and retrieve results containing the specified risk level. You can specify multiple comma-separated risk levels to retrieve code repositories containing the specified risk levels. For example, LOW,MEDIUM,HIGH.
</td></tr><tr><td>Attribute Type</td><td>(Optional) Specify an attribute type to search in code repositories and retrieve results containing the specified attribute type. You can specify multiple comma-separated attribute types to retrieve code repositories containing the specified attribute types. For example, Email,Password.
</td></tr><tr><td>Status</td><td>(Optional) Select a status to search in code repositories and retrieve results containing the specified status. You can select from following options: Active Ignored Resolved
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when a profile was added. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when a profile was added. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "id": "",
            "repo_url": "",
            "files_count": "",
            "risk_level": "",
            "attribute": "",
            "matched_domain": "",
            "attribute_type": "",
            "added_ts": "",
            "status": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Code Repos Statistics
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count_by_action": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_attribute_type": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            },
            {
                "count": "",
                "id": ""
            },
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_risk_level": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            },
            {
                "count": "",
                "id": ""
            },
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    }
}</pre>

### operation: Get Code Repo Matched Domains Statistics
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count_by_matched_domain": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    }
}</pre>

### operation: Get Domain Threats
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search By Keyword</td><td>(Optional) Specify a keyword to search in domain threats and retrieve results containing the specified keyword. The keyword is searched in domain, URL, severity, original domain, online status, and fuzzer fields.
</td></tr><tr><td>Original Domain</td><td>(Optional) Specify a domain to search in domain threats and retrieve results containing the specified domain name. You can specify multiple comma-separated domains to retrieve domain threats containing the specified domains. For example: domain1.com,domain2.com.
</td></tr><tr><td>Tags</td><td>(Optional) Specify a tag to search in domain threats and retrieve results containing the specified tags. You can specify multiple tags to retrieve domain threats containing the specified tags. For example: b7c4409f4e34eedc7a5447b077732c66,b7c4409f4e34eedc7a5447b077732c77. NOTE: Tag ID can be retrieved from the Get Tags action.
</td></tr><tr><td>Online Status</td><td>(Optional) Select an online status search in domain threats and retrieve results containing the specified online status. You can select one of the following options: Online Not Available Non Functional Offline
</td></tr><tr><td>Status</td><td>(Optional) Select a status to search in domain threats and retrieve results containing the specified status. You can select from following options: Active Ignored Resolved
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when a profile was added. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when a profile was added. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "added_ts": "",
            "domain": "",
            "expiration_date": "",
            "fuzzer": "",
            "id": "",
            "is_false_positive": "",
            "is_impersonation": "",
            "is_parked": "",
            "online_status": "",
            "original_domain": "",
            "registration_date": "",
            "severity": "",
            "source": "",
            "source_name": "",
            "status": "",
            "tags": []
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Domain Threats By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain Threat ID</td><td>Specify an ID of the domain threat to retrieve its details.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "added_ts": "",
    "domain": "",
    "id": "",
    "notable_change_ts": "",
    "ticket_id": "",
    "is_false_positive": "",
    "is_impersonation": "",
    "is_parked": "",
    "online_status": "",
    "original_domain": "",
    "severity": "",
    "source": "",
    "source_name": "",
    "status": "",
    "tags": [
        {
            "id": "",
            "name": ""
        }
    ]
}</pre>

### operation: Get Executive Exposures
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Source Type</td><td>(Optional) Specify a source type in which to search and retrieve results containing the specified Executive ID.
</td></tr><tr><td>Executive ID</td><td>(Optional) Specify an executive ID to search and retrieve results containing the specified executive ID.
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when a report was added. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when a report was added. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "added_ts": "",
            "data": {},
            "executive_id": "",
            "id": "",
            "matched_keywords": [
                {
                    "type": "",
                    "value": ""
                }
            ],
            "source_type": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Executive Profiles
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Executive Name</td><td>(Optional) Specify an executive name to search and retrieve results containing the specified executive's name.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "id": "",
            "name": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Open Bucket Exposures
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search By Keyword</td><td>(Optional) Specify a keyword to search in open bucket exposures and retrieve results containing the specified keyword.
</td></tr><tr><td>File Type</td><td>(Optional) Specify a file type to search in open bucket exposures and retrieve results containing the specified file types. You can specify multiple comma-separated file types to retrieve open bucket exposures containing the specified file types. For example gz,tgz,docx.
</td></tr><tr><td>Bucket Type</td><td>(Optional) Specify a bucket type to search in open bucket exposures and retrieve results containing the specified bucket types. You can specify multiple comma-separated bucket types to retrieve open bucket exposures containing the specified bucket types. For example gcp,aws,azure.
</td></tr><tr><td>Status</td><td>(Optional) Select a status to search in open bucket exposures and retrieve results containing the specified status. You can select from following options: Active Ignored Resolved
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when a profile was added. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when a profile was added. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "accessibility_status": "",
            "added_ts": "",
            "bucket": "",
            "bucket_id": "",
            "bucket_type": "",
            "file_name": "",
            "file_size": "",
            "file_type": "",
            "full_path": "",
            "id": "",
            "source_id": "",
            "status": "",
            "url": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Rogue Apps
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Status</td><td>(Optional) Select the rogue apps status type from the following options to filter the results: Unofficial: These are the apps that are not necessarily rouge but mention your organization's brand, OFFICIAL: These are the apps that are officially published by your organization, ROGUE: These are the apps that are deemed to be impersonating your organization, TAKEDOWN: These are the rouge apps that are currently undergoing takedown by FortiRecon, ALSE_POSITIVE: These are the apps that were classified as either rouge or unofficial but are now deemed to be false positives by your organization's analysts, RESOLVED: These are the rouge apps that have been taken down.
</td></tr><tr><td>Search By Keyword</td><td>(Optional) Specify a keyword to search in rogue apps and retrieve results containing the specified keyword.
</td></tr><tr><td>App Store Name</td><td>(Optional) Specify a app store to search in rogue apps and retrieve results containing the specified app stores. You can specify multiple comma-separated file types to retrieve rogue apps containing the specified file types. For example Androidapk,Applestore.
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when a rogue app was first seen. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when a rogue app was first seen. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default page is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "added_ts": "",
            "app_name": "",
            "app_size": "",
            "appstore": "",
            "description": "",
            "developer_name": "",
            "download_count": "",
            "download_url": "",
            "first_seen": "",
            "id": "",
            "keyword": "",
            "package_name": "",
            "status": "",
            "ticket_id": "",
            "updated_ts": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Rogue App By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Rogue App ID</td><td>Specify the ID of the rogue app to get its details.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "app_name": "",
    "app_size": "",
    "appstore": "",
    "description": "",
    "developer_name": "",
    "developer_url": "",
    "download_count": "",
    "download_url": "",
    "first_seen": "",
    "id": "",
    "is_whitelisted": "",
    "keyword": "",
    "last_seen": "",
    "listing_url": "",
    "package_name": "",
    "review_count": "",
    "review_stars": "",
    "screenshot_url": "",
    "status": "",
    "ticket_id": "",
    "updated_ts": ""
}</pre>

### operation: Get Social Media Threats
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search By Keyword</td><td>(Optional) Specify a keyword to search in social media threats and retrieve results containing the specified keyword in profile name or handle name fields.
</td></tr><tr><td>Media Type</td><td>(Optional) Specify a social media platform to search in social media threats and retrieve results containing the specified social media platforms. You can specify multiple comma-separated social media platforms to retrieve social media threats containing the specified social media platforms. For example FACEBOOK,INSTAGRAM,TWITTER.
</td></tr><tr><td>Profile Name</td><td>(Optional) Specify a profile name to search and retrieve social media threats containing the specified profile name.
</td></tr><tr><td>Handle Name</td><td>(Optional) Specify a handle name to search and retrieve social media threats containing the specified handle name.
</td></tr><tr><td>Is Verified</td><td>(Optional) Select whether the profile or the handle name is verified to retrieve social media threats containing only verified profile or handle name. You can select one of the following options: True False
</td></tr><tr><td>Status</td><td>(Optional) Select a status to search in social media threats and retrieve results containing the specified status. You can select from following options: Active False Positive Takedown Resolved
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when a profile was added. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when a profile was added. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "added_ts": "",
            "followers_count": "",
            "friends_count": "",
            "handle_name": "",
            "id": "",
            "is_verified": "",
            "location": "",
            "media_type": "",
            "posts_count": "",
            "profile_creation_ts": "",
            "profile_name": "",
            "profile_url": "",
            "source_id": "",
            "status": "",
            "ticket_id": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Get Domain Threats Statistics
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count_by_action": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_domain_status": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_tags": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    }
}</pre>

### operation: Get Original Domains Statistics
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count_by_original_domain": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    }
}</pre>

### operation: Get Open Bucket Exposures Statistics
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count_by_accessibility_status": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_bucket_type": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_file_type": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_status": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    }
}</pre>

### operation: Get Social Media Threats Statistics
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count_by_is_verified": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_media_type": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    },
    "count_by_status": {
        "aggregations": [
            {
                "count": "",
                "id": ""
            }
        ],
        "total": ""
    }
}</pre>

### operation: Get Tags
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "id": "",
            "name": ""
        }
    ]
}</pre>

### operation: Get Takedown Requests
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search By Keyword</td><td>(Optional) Specify a keyword to search in takedown requests and retrieve results containing the specified keyword.
</td></tr><tr><td>Status</td><td>(Optional) Select a status to search in take-down requests and retrieve results containing the specified status. You can select from following options: REQUESTED, ACKNOWLEDGED, REJECTED, APPROVED, INITIATED, SUCCESSFULLY_CLOSED, UNSUCCESSFULLY_CLOSED.
</td></tr><tr><td>Category</td><td>(Optional) Select a category to search in take-down requests and retrieve results containing the specified category. you can select from the following options: DomainThreat, RogueApps, SocialMediaThreat.
</td></tr><tr><td>Start Date</td><td>(Optional) Select the start date of the range containing the date when the takedown was requested. Selecting a start date is mandatory if an End Date is selected.
</td></tr><tr><td>End Date</td><td>(Optional) Select the end date of the range containing the date when the takedown was requested. Default is the current date.
</td></tr><tr><td>Page</td><td>(Optional) Specify the page number from which to retrieve the results. Default value is 1.
</td></tr><tr><td>Size</td><td>(Optional) Specify the number of records to fetch per page. Default value is 10 and you can specify a maximum value of 500 per page.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "hits": [
        {
            "added_ts": "",
            "category": "",
            "entity": "",
            "id": "",
            "resource_id": "",
            "status": "",
            "ticket_id": ""
        }
    ],
    "page": "",
    "size": "",
    "total": ""
}</pre>

### operation: Update Code Repo Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Code Repo ID</td><td>Specify the Code Repo ID to update the status.
</td></tr><tr><td>Status</td><td>Specify the status to update the Code Repo. You can choose from ACTIVE, RESOLVED, IGNORED.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": ""
}</pre>

### operation: Update Domain Threat Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain Threat ID</td><td>Specify the Domain Threat ID to update the status.
</td></tr><tr><td>Status</td><td>Specify the status to update the Domain Threat. You can choose from ACTIVE, RESOLVED, FALSE_POSITIVE, TAKEDOWN, SAFELIST.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": ""
}</pre>

### operation: Update Open Bucket Exposure Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Open Bucket Exposure ID</td><td>Specify the Open Bucket Exposure ID to update the status.
</td></tr><tr><td>Status</td><td>Specify the status to update the Open Bucket Exposure. You can choose from ACTIVE, RESOLVED, IGNORED.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": ""
}</pre>

### operation: Update Rogue App Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Rogue App ID</td><td>Specify the Rogue App ID to update the status.
</td></tr><tr><td>Status</td><td>Specify the status to update the Rogue App. You can choose from UNOFFICIAL, RESOLVED, FALSE_POSITIVE, OFFICIAL, ROGUE, TAKEDOWN.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": ""
}</pre>

### operation: Update Social Media Threat Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Social Media Threat ID</td><td>Specify the Social Media Threat ID to update the status.
</td></tr><tr><td>Status</td><td>Specify the status to update the Social Media Threat. You can choose from ACTIVE, FALSE_POSITIVE, TAKEDOWN.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": ""
}</pre>
## Included playbooks
The `Sample - fortinet-fortirecon-brand-protection - 2.1.0` playbook collection comes bundled with the Fortinet FortiRecon Brand Protection connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Fortinet FortiRecon Brand Protection connector.

- Get Code Repo Exposures
- Get Code Repositories
- Get Code Repos Statistics
- Get Code Repo Matched Domains Statistics
- Get Domain Threats
- Get Domain Threats By ID
- Get Executive Exposures
- Get Executive Profiles
- Get Open Bucket Exposures
- Get Rogue Apps
- Get Rogue App By ID
- Get Social Media Threats
- Get Domain Threats Statistics
- Get Original Domains Statistics
- Get Open Bucket Exposures Statistics
- Get Social Media Threats Statistics
- Get Tags
- Get Takedown Requests
- Update Code Repo Status
- Update Domain Threat Status
- Update Open Bucket Exposure Status
- Update Rogue App Status
- Update Social Media Threat Status

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
