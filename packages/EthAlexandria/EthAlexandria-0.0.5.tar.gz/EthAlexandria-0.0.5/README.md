
# Alexandria

A project to decentralize and distribute literary infrastructure.

See [github](https://github.com/ObiajuluM/Alexandria#alexandria) for a detailed breakdown.





## Usage/Examples

```python
import EthAlexandria # import the package
import ipfshttpclient # for connecting to ipfs


# url to connect to 
NETWORK = "https://mainnet.infura.io/v3/"
# currently supports Polygon, Binance Smart Chain, Evmos, etc.


# create an instance of the objects
contract_book = EthAlexandria.Book(NETWORK) # instance of the contract book

ipfs_book = EthAlexandria.BookIPFS(NETWORK) # instance of the ipfs book

library = EthAlexandria.Library(NETWORK) # instance of library

mnemonic = "your mnemonic here"

# ALWAYS LOAD_DATA(), before you begine working with the contract
contract_book.load_data()
ipfs_book.load_data()
library.load_data()


# Load the addresses of already deployed contracts [ignore]
contract_book_address = "0xAD94E1Fd0158C64981D29B03eE0C4C350C5b0B69"
ipfs_book_address = "0x98126F0d49e3137355B71f708Bb564ff9f224ED7"
library_address = "0x80303A8EBF84aeDf25c75ea5e2C474b4aE6dFe3A"

# generate new contracts and return their addresses

# generate a new book contract
print(contract_book.new_book("Rich Dad", "MIT", mnemonic).contractAddress)

# generate a new ipfs contract book, this method deploys the book directly to ipfs before contract deployment
print(ipfs_book.new_ipfs_book("Rich Dad", "MIT", "rich_dad.pdf", "pdf", client, mnemonic).contractAddress)

# generate a new library contract
print(library.new_library("Library of Alexandria", mnemonic).contractAddress)
```

All the available methods


`EthAlexandria.Book`

``` python 
Method: deposit_ether_to_contract()
Doc: Deposit ether to the contract

Method: get_all_time_value()
Doc: return book all time value

Method: get_author()
Doc: return book author

Method: get_book_balance()
Doc: return book balance

Method: get_book_license()
Doc: return book book_license

Method: get_chapter_content()
Doc: return book chapter content

Method: get_chapter_name()
Doc: return book chapter name

Method: get_chapter_status()
Doc: return book chapter status

Method: get_chapters_count()
Doc: return book chapters count

Method: get_title()
Doc: return book title

Method: load_data()
Doc: load neccessary data to work with the object

Method: new_book()
Doc: create new book

Method: new_chapter()
Doc: create new chapter

Method: remove_chapter()
Doc: remove chapter

Method: transfer_ether_from_book_contract()
Doc: transfer ether from contract
```

   

`EthAlexandria.BookIPFS`
``` python 
Method: deposit_ether_to_contract()
Doc: Deposit ether to the contract

Method: get_all_time_value()
Doc: return book all time value

Method: get_author()
Doc: return book author

Method: get_book_format()
Doc: return book format as deployed to ipfs, used to build the book from the hash

Method: get_book_license()
Doc: return book book_license

Method: get_ipfs_book_balance()
Doc: return book balance

Method: get_ipfs_hash()
Doc: return book ipfs hash

Method: get_title()
Doc: return book title

Method: load_data()
Doc: load neccessary data to work with the object

Method: new_ipfs_book()
Doc: create new ipfs book this is also upload the book to ipfs

Method: resolve_book_from_ipfs()
Doc: return the book from ipfs

Method: transfer_ether_from_book_contract()
Doc: transfer ether from contract

Method: upload_to_ipfs()
Doc: upload book to ipfs

```

`EthAlexandria.Library`

``` python
Method: add_book()
Doc: add book to library

Method: deposit_ether_to_contract()
Doc: Deposit ether to the contract

Method: get_all_time_value()
Doc: return library all time value

Method: get_book_address()
Doc: return book address

Method: get_book_author()
Doc: return book author

Method: get_book_count()
Doc: return book count

Method: get_book_status()
Doc: return book status

Method: get_book_title()
Doc: return book title

Method: get_librarian()
Doc: return library librarian

Method: get_library_balance()
Doc: get library balance

Method: get_library_name()
Doc: return library name

Method: get_quote()
Doc: return library quote

Method: load_data()
Doc: load neccessary data to work with the object

Method: new_library()
Doc: create new library

Method: remove_book()
Doc: remove book from library

Method: transfer_ether_from_library_contract()
Doc: transfer ether from library contract

Method: transfer_position()
Doc: transfer librarian position

```


## License

[MIT](https://choosealicense.com/licenses/mit/)

