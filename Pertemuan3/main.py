from block import Block
from pow import proof_of_work
from pos import proof_of_stake

print("PROOF OF WORK")

difficulty = 3
chain = []

data_list = [
    {
        "id_lagu": "SING-001",
        "judul": "Secret Lover",
        "actor": "Ghiyas Muharraran",
        "pemegang_hak_cipta": "Ghiyas Music Studio",
        "tahun": 2030,
    },
    {
        "id_lagu": "SING-001",
        "platform": "Spotify",
        "jumlah_pendengar": 2000000,
        "royalti": "Rp. 250.000",
    },
    {
        "id_lagu": "SING-001",
        "platform": "Youtube",
        "jumlah_penonton": 3000000,
        "royalti": "Rp. 200.000",
    },
    {
        "id_lagu": "SING-001",
        "penerima": "Ghiyas Muharraran",
        "jumlah_pembayaran": "Rp. 450.000",
        "status_pembayaran": "sudah dibayar",
    },
]

previous_hash = "0"

for i, data in enumerate(data_list):
    block = Block(i + 1, data, previous_hash)

    print(f"\nMenambang Block #{block.index} ...")

    proof_of_work(block, difficulty)

    print("Data Block :", block.data)
    print("Nonce      :", block.nonce)
    print("Hash       :", block.hash)

    chain.append(block)

    previous_hash = block.hash


def is_chain_valid(chain, difficulty):
    target = "0" * difficulty

    for i in range(len(chain)):
        block = chain[i]

        if block.hash != block.calculate_hash():
            return False

        if not block.hash.startswith(target):
            return False

        if i > 0:
            if block.previous_hash != chain[i - 1].hash:
                return False

    return True


print("\nBlockchain valid:", is_chain_valid(chain, difficulty))


print("\nPROOF OF STAKE")

validators = {
    "Ghiyas Music Studio": 10,
    "Spotify": 20,
    "Youtube": 20,
    "Distributor Royalti": 30,
}

print("\nValidator:")

for validator, stake in validators.items():
    print(f"- {validator}: {stake} stake")

selected = proof_of_stake(validators)

print("\nValidator terpilih:", selected)