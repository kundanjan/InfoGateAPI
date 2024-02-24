from dotenv import load_dotenv
from eth_account import Account
from flask import Flask, jsonify, request
from web3 import Web3
import json
from credentials import details

load_dotenv()
Account.enable_unaudited_hdwallet_features()

# Create an instance of the Flask class
app = Flask(__name__)



w3 = Web3(Web3.HTTPProvider(details.provider_url))

# Set the address of the deployed contract
monitor_contract_address = '0xc365306F7d00C095AA3f1768307F054f4127616B'
cpu_contract_address='0x9AdD894a3F727660CAc12C1c807550958A3e29C4'

# ABI (Application Binary Interface) of the smart contract
monitor_contract_abi = [{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'MonitorAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addMonitor', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'getAllMonitorIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getMonitorById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'monitorCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]

# Create contract object
monitor_contract = w3.eth.contract(address=monitor_contract_address, abi=monitor_contract_abi)

cpu_contract_abi = [{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'CPUAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addCPU', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'cpuCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getAllCPUIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getCPUById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}]

# Create contract object
cpu_contract = w3.eth.contract(address=cpu_contract_address, abi=cpu_contract_abi)

# Define a route using a Python decorator
@app.route("/")  # Decorator defines a GET request handler for the root path
def read_root():
    return jsonify({"message": "Hello, world!"})

# Uncomment the following route to handle path parameters
@app.route('/get_monitor_info/<int:monitor_id>', methods=['GET'])
def get_monitor_info(monitor_id):
    try:
        # Call the getMonitorById function
        monitor_info = monitor_contract.functions.getMonitorById(monitor_id).call()

        # Format monitor information
        monitor_info_dict = {
            "id": monitor_info[0],
            "name_of_brand": monitor_info[1],
            "suppliers_full_address": monitor_info[2],
            "date_of_receipt_of_computer": monitor_info[3],
            "cost_of_computer": monitor_info[4],
            "dsr_page_no_and_sr_no": monitor_info[5],
            "name_of_department": monitor_info[6],
            "name_of_laboratory": monitor_info[7]
        }

        return jsonify({"monitor_info": monitor_info_dict}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/add_monitor', methods=['POST'])
def add_monitor():
    # Account from which you want to send the transaction
    private_key = Account.from_mnemonic(details.phrase)._private_key.hex()

    try:
        # Get parameters from the request JSON
        request_data = request.json
        name_of_brand = request_data.get('name_of_brand')
        suppliers_full_address = request_data.get('suppliers_full_address')
        date_of_receipt_of_computer = request_data.get('date_of_receipt_of_computer')
        cost_of_computer = request_data.get('cost_of_computer')
        dsr_page_no_and_sr_no = request_data.get('dsr_page_no_and_sr_no')
        name_of_department = request_data.get('name_of_department')
        name_of_laboratory = request_data.get('name_of_laboratory')

        # Call the addMonitor function
        tx_hash = monitor_contract.functions.addMonitor(
            name_of_brand,
            suppliers_full_address,
            date_of_receipt_of_computer,
            cost_of_computer,
            dsr_page_no_and_sr_no,
            name_of_department,
            name_of_laboratory
        ).build_transaction({
            "from": details.account_address,
            'nonce': w3.eth.get_transaction_count(details.account_address),
            "gas": 20000000,
            'gasPrice': w3.to_wei('50', 'gwei'),  # Adjust gas limit as needed
        })

        # Sign transaction
        signed_txn = w3.eth.account.sign_transaction(tx_hash, private_key=private_key)

        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        # json_data = json.dumps(dict({"transaction_receipt": tx_receipt}))
        # return json_data
        print(tx_receipt)
        tx_receipt_dict=dict(tx_receipt)
        return jsonify({"transaction_hash":tx_receipt_dict['transactionHash'].hex()})
    
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_cpu_info/<int:cpu_id>', methods=['GET'])
def get_cpu_info(cpu_id):
    try:
        # Call the getMonitorById function
        Cpu_info = cpu_contract.functions.getCPUById(cpu_id).call()

        # Format monitor information
        cpu_info_dict = {
            "id": Cpu_info[0],
            "name_of_brand": Cpu_info[1],
            "suppliers_full_address": Cpu_info[2],
            "date_of_receipt_of_computer": Cpu_info[3],
            "cost_of_computer": Cpu_info[4],
            "dsr_page_no_and_sr_no": Cpu_info[5],
            "name_of_department": Cpu_info[6],
            "name_of_laboratory": Cpu_info[7]
        }

        return jsonify({"cpu_info": cpu_info_dict}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/add_cpu', methods=['POST'])
def add_cpu():
    # Account from which you want to send the transaction
    private_key = Account.from_mnemonic(details.phrase)._private_key.hex()

    try:
        # Get parameters from the request JSON
        request_data = request.json
        name_of_brand = request_data.get('name_of_brand')
        suppliers_full_address = request_data.get('suppliers_full_address')
        date_of_receipt_of_computer = request_data.get('date_of_receipt_of_computer')
        cost_of_computer = request_data.get('cost_of_computer')
        dsr_page_no_and_sr_no = request_data.get('dsr_page_no_and_sr_no')
        name_of_department = request_data.get('name_of_department')
        name_of_laboratory = request_data.get('name_of_laboratory')

        # Call the addMonitor function
        tx_hash = cpu_contract.functions.addCPU(
            name_of_brand,
            suppliers_full_address,
            date_of_receipt_of_computer,
            cost_of_computer,
            dsr_page_no_and_sr_no,
            name_of_department,
            name_of_laboratory
        ).build_transaction({
            "from": details.account_address,
            'nonce': w3.eth.get_transaction_count(details.account_address),
            "gas": 20000000,
            'gasPrice': w3.to_wei('50', 'gwei'),  # Adjust gas limit as needed
        })

        # Sign transaction
        signed_txn = w3.eth.account.sign_transaction(tx_hash, private_key=private_key)

        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        # json_data = json.dumps(dict({"transaction_receipt": tx_receipt}))
        # return json_data
        print(tx_receipt)
        tx_receipt_dict=dict(tx_receipt)
        return jsonify({"transaction_hash":tx_receipt_dict['transactionHash'].hex()})
    
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
