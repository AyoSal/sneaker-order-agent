from google.adk.agents import Agent
from .prompts import ROOT_AGENT_INSTR
from .sendgrid_connector_tool import sendgrid_connector_tool
from .get_address_ahub_tool import get_address_ahub_tool
from .get_shoes_ahub_tool import shoes_ahub_tool 
#from .get_shoes_ahub_tool import shoes_ahub_tool
#from .order_tool import create_order_tool
from .order_ahub_tool import orders_ahub_tool



import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='sneaker_order_agent',
    description="Agent to create orders, confirm location and send email",
    instruction=ROOT_AGENT_INSTR,
    tools=[shoes_ahub_tool, get_address_ahub_tool, orders_ahub_tool, sendgrid_connector_tool]
)

