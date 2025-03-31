from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Nhập các giao dịch từ bàn phím
print("=== Nhập giao dịch ===")
while True:
    sender = input("Người gửi: ")
    receiver = input("Người nhận: ")
    try:
        amount = float(input("Số tiền: "))
    except ValueError:
        print("Số tiền không hợp lệ. Vui lòng thử lại.")
        continue

    my_blockchain.add_transaction(sender, receiver, amount)

    cont = input("Bạn có muốn thực hiện thêm giao dịch nữa không? (1/0): ")#1: la tiep tuc giao dich khac // 0: thoat giao dich
    if cont.lower() != '1':
        break

# Mining block sau khi nhập giao dịch
print("\n=== Đang thực hiện đào block... ===")
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

# Thêm phần thưởng cho thợ đào
my_blockchain.add_transaction('Genesis', 'Miner', 1)

new_block = my_blockchain.create_block(new_proof, previous_hash)
print(" Block mới đã được tạo!")

# Hiển thị toàn bộ blockchain
print("\n=== Chuỗi khối hiện tại ===")
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-" * 40)

# Kiểm tra tính hợp lệ của blockchain
print("\n Blockchain hợp lệ:", my_blockchain.is_chain_valid(my_blockchain.chain))
