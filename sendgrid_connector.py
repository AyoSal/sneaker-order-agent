from dotenv import load_dotenv
from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset

sendgrid_connector_tool = ApplicationIntegrationToolset(
    project="{YOUR PROJECT}",
    location="{REGION}",
    connection="sendgrid-email",
    ##entity_operations= {"A_SalesOrder": ["GET","LIST","CREATE"]},
    actions=["SendMail2"],
    ##service_account_credentials='{...}', # optional
    tool_instructions="""Use this tool to send email to customers, the request should be in the format 
FromName: "{NAME}"
FromEmail: "{EMAIL ADDRESS}"
Personalizations: "[{"to": [{"email": {{customer email}}}]}]"
Content: "[{"type": "text/plain", "value": {{email message}}}]"""
)
