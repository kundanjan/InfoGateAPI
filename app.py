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
mouse_contract_address ='0x678327150a7a3BA74bD0892e6E213544dAaFc119'
keyboard_contract_address ='0x5c34b0015fBd7FFb95EcFa0F2923533Acd31986A'
printer_contract_address ='0x941CDb973442b80a0e9317167A7Fe0B13e90e3C0'
scanner_contract_address ='0xEA234F25B7Ad709066Ac6Ff91AeA1Be010413076'

# ABI (Application Binary Interface) of the smart contract
monitor_contract_abi = [{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'MonitorAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addMonitor', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'getAllMonitorIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getMonitorById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'monitorCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]
monitor_contract = w3.eth.contract(address=monitor_contract_address, abi=monitor_contract_abi)

cpu_contract_abi = [{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'CPUAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addCPU', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'cpuCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getAllCPUIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getCPUById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}]
cpu_contract = w3.eth.contract(address=cpu_contract_address, abi=cpu_contract_abi)

mouse_contract_abi=[{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'MouseAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addMouse', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'getAllMouseIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getMouseById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'mouseCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]
mouse_contract=w3.eth.contract(address=mouse_contract_address, abi=mouse_contract_abi)

keyboard_contract_abi=[{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'KeyboardAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addKeyboard', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'getAllKeyboardIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getKeyboardById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfComputer', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfComputer', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'keyboardCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]
keyboard_contract=w3.eth.contract(address=keyboard_contract_address, abi=keyboard_contract_abi)

printer_contract_abi=[{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'PrinterAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfPrinter', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfPrinter', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addPrinter', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'getAllPrinterIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getPrinterById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfPrinter', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfPrinter', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'printerCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]
printer_contract=w3.eth.contract(address=printer_contract_address, abi=printer_contract_abi)

scanner_contract_abi=[{'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}], 'name': 'ScannerAdded', 'type': 'event'}, {'inputs': [{'internalType': 'string', 'name': '_nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': '_suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': '_dateOfReceiptOfScanner', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_costOfScanner', 'type': 'uint256'}, {'internalType': 'string', 'name': '_dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': '_nameOfLaboratory', 'type': 'string'}], 'name': 'addScanner', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'getAllScannerIds', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'getScannerById', 'outputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'string', 'name': 'nameOfBrand', 'type': 'string'}, {'internalType': 'string', 'name': 'suppliersFullAddress', 'type': 'string'}, {'internalType': 'uint256', 'name': 'dateOfReceiptOfScanner', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'costOfScanner', 'type': 'uint256'}, {'internalType': 'string', 'name': 'dsrPageNoAndSRNo', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfDepartment', 'type': 'string'}, {'internalType': 'string', 'name': 'nameOfLaboratory', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'scannerCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]
scanner_contract=w3.eth.contract(address=scanner_contract_address, abi=scanner_contract_abi)


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
            "date_of_receipt_of_computer": int(monitor_info[3]),
            "cost_of_computer": int(monitor_info[4]),
            "dsr_page_no_and_sr_no": monitor_info[5],
            "name_of_department": monitor_info[6],
            "name_of_laboratory": monitor_info[7]
        }

        return jsonify({"monitor_info": monitor_info_dict}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('a', methods=['POST'])
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
    
@app.route('/get_mouse_info/<int:mouse_id>', methods=['GET'])
def get_mouse_info(mouse_id):
    try:
        # Call the getMonitorById function (assuming it exists in your contract)
        mouse_info = mouse_contract.functions.getMouseById(mouse_id).call()

        # Format mouse information
        mouse_info_dict = {
            "id": mouse_info[0],
            "name_of_brand": mouse_info[1],
            "suppliers_full_address": mouse_info[2],
            "date_of_receipt_of_computer": mouse_info[3],
            "cost_of_computer": mouse_info[4],
            "dsr_page_no_and_sr_no": mouse_info[5],
            "name_of_department": mouse_info[6],
            "name_of_laboratory": mouse_info[7]
        }

        return jsonify({"mouse_info": mouse_info_dict}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add_mouse', methods=['POST'])
def add_mouse():
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
        tx_hash = mouse_contract.functions.addMouse(
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
        tx_receipt_dict=dict(tx_receipt)
        return jsonify({"transaction_hash":tx_receipt_dict['transactionHash'].hex()})


    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/get_keyboard_info/<int:keyboard_id>', methods=['GET'])
def get_keyboard_info(keyboard_id):
    try:
        # Call the getMonitorById function (assuming it exists in your contract)
        keyboard_info = keyboard_contract.functions.getKeyboardById(keyboard_id).call()

        # Format keyboard information
        keyboard_info_dict = {
            "id": keyboard_info[0],
            "name_of_brand": keyboard_info[1],
            "suppliers_full_address": keyboard_info[2],
            "date_of_receipt_of_computer": keyboard_info[3],
            "cost_of_computer": keyboard_info[4],
            "dsr_page_no_and_sr_no": keyboard_info[5],
            "name_of_department": keyboard_info[6],
            "name_of_laboratory": keyboard_info[7]
        }

        return jsonify({"keyboard_info": keyboard_info_dict}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add_keyboard', methods=['POST'])
def add_keyboard():
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
        tx_hash = keyboard_contract.functions.addKeyboard(
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
        tx_receipt_dict=dict(tx_receipt)
        return jsonify({"transaction_hash":tx_receipt_dict['transactionHash'].hex()})


    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/get_printer_info/<int:printer_id>', methods=['GET'])
def get_printer_info(printer_id):
    try:
        # Call the getMonitorById function (assuming it exists in your contract)
        printer_info = printer_contract.functions.getPrinterById(printer_id).call()

        # Format printer information
        printer_info_dict = {
            "id": printer_info[0],
            "name_of_brand": printer_info[1],
            "suppliers_full_address": printer_info[2],
            "date_of_receipt_of_computer": printer_info[3],  # Consider renaming for clarity
            "cost_of_computer": printer_info[4],            # Consider renaming for clarity
            "dsr_page_no_and_sr_no": printer_info[5],
            "name_of_department": printer_info[6],
            "name_of_laboratory": printer_info[7]
        }

        return jsonify({"printer_info": printer_info_dict}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add_printer', methods=['POST'])
def add_printer():
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
        tx_hash = printer_contract.functions.addPrinter(
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
        tx_receipt_dict=dict(tx_receipt)
        return jsonify({"transaction_hash":tx_receipt_dict['transactionHash'].hex()})


    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/get_scanner_info/<int:scanner_id>', methods=['GET'])
def get_scanner_info(scanner_id):
    try:
        # Call the getMonitorById function (assuming it exists in your contract)
        scanner_info = scanner_contract.functions.getScannerById(scanner_id).call()

        # Format scanner information
        scanner_info_dict = {
            "id": scanner_info[0],
            "name_of_brand": scanner_info[1],
            "suppliers_full_address": scanner_info[2],
            "date_of_receipt_of_computer": scanner_info[3],  # Consider renaming for clarity
            "cost_of_computer": scanner_info[4],            # Consider renaming for clarity
            "dsr_page_no_and_sr_no": scanner_info[5],
            "name_of_department": scanner_info[6],
            "name_of_laboratory": scanner_info[7]
        }

        return jsonify({"scanner_info": scanner_info_dict}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add_scanner', methods=['POST'])
def add_scanner():
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
        tx_hash = scanner_contract.functions.addScanner(
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
        tx_receipt_dict=dict(tx_receipt)
        return jsonify({"transaction_hash":tx_receipt_dict['transactionHash'].hex()})


    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Run the Flask application
# if __name__ == "__main__":
#     app.run(debug=True)
