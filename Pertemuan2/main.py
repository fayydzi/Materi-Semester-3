from blockchain import Blockchain


blockchain = Blockchain()

# regis hak cipta lagu
blockchain.add_block({
    "id_lagu": "SING-001",
    "judul": "Secret lover",
    "actor": "Ghiyas Muharraran",
    "Pemegang_Hak_Cipta": "Ghiyas Music Studio",
    "tahun": 2030,
})

# royalti spotify
blockchain.add_block({
    "id_lagu": "SING-001",
    "platform": "Spotify",
    "jumlah_pendengar": 2000000,
    "royalti": "Rp. 250.000",
    "mata_uang": "USD",
})

# royalti youtube
blockchain.add_block({
    "id_lagu": "SING-001",
    "platform": "Youtube",
    "jumlah_penonton": 3000000,
    "royalti": "Rp. 200.000",
    "mata_uang": "USD",
})

# pembayaran royalti
blockchain.add_block({
    "id_lagu": "SING-001",
    "penerima": "Ghiyas Muharraran",
    "jumlah_pembayaran": "Rp. 450.000",
    "status_pembayaran": "sudah dibayar",
})

for block in blockchain.chain:
    print("=" * 50)
    print("INDEX :", block.index)
    print("TIME :", block.timestamp)
    print("DATA :", block.data)
    print("PREV :", block.previous_hash)
    print("HASH :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())