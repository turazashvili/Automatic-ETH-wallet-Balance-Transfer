<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<a href="https://www.buymeacoffee.com/axrisi" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>



<!-- PROJECT LOGO -->
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project represents script allowing you create a loop of constant/automatic requests to your wallet withdrawing the balance. At this moment it does it for only native token of the chain you use: ETH, MATIC, BNB, AVAX etc.

There are multiple usecases for this:
  1) You might need to redirect incoming transaction from multiple wallets to the main one.
  2) You might need to protect your account and set up script when you are not using the wallet, and shutting the script off only when you need to      make some transactions and back on when you are done.
  3) You might somehow disposed your private keys and want to protect other tokens you have on wallet. So emptying the wallet balance will prevent      scammers making any other transaction.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [Web3](https://pypi.org/project/web3/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer.git
   ```
2. Install Python
   Choose latest release for your OS https://www.python.org/downloads/
3. Enter your Wallets and Key in `loop.py`
   ```py
   private_key = "<Your_Private_Key"
   pub_key ="<Your_wallet>"
   recipient_pub_key = "<Recipient_wallet>"
   ```
4. Enter your gasPrice, gasLimit and chainId in `loop.py`
   ```py
    gasPrice = w3.toWei('30', 'gwei')
    gasLimit = 21000
    
    tx = {
            'chainId': 3,
   ```
   You can find your chain ID here: https://chainlist.wtf/.<br></br>
   Your current required gasPrice in gwei here: 
     * [Ethereum](https://etherscan.io/gastracker)
     * [Polygon](https://polygonscan.com/gastracker)
     * [Binance](https://bscscan.com/gastracker)
     * [Avalanche]( https://snowtrace.io/gastracker)

5. Add the Endpoint for the chain you chose.
   ```py
   w3 = Web3(Web3.HTTPProvider(<Moralis or Infura_endpoint_link>)
   ```
   Visit https://moralis.io or https://infura.io/ or any other endpoint you can find.

6. Run the script
   ```py
    python loop.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<img width="220" alt="image" src="https://user-images.githubusercontent.com/74835523/172040143-9e39478d-fc9c-4fe8-843c-bc27ecfeeea0.png">


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add API support for GAS fees
- [ ] Add local ETH miner endpoint to refer quicker to chain and bypass API request limits
- [ ] Edit script for it to check the incoming transaction in pending transactions in mempool


See the [open issues](https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nikoloz Turazashvili - [@axrisi](https://twitter.com/axrisi) - turazashvili@gmail.com

Project Link: [https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/](https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/turazashvili/Automatic-ETH-wallet-Balance-Transfer.svg?style=for-the-badge
[contributors-url]: https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/turazashvili/Automatic-ETH-wallet-Balance-Transfer.svg?style=for-the-badge
[forks-url]: https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/network/members
[stars-shield]: https://img.shields.io/github/stars/turazashvili/Automatic-ETH-wallet-Balance-Transfer.svg?style=for-the-badge
[stars-url]: https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/stargazers
[issues-shield]: https://img.shields.io/github/issues/turazashvili/Automatic-ETH-wallet-Balance-Transfer.svg?style=for-the-badge
[issues-url]: https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/issues
[license-shield]: https://img.shields.io/github/license/turazashvili/Automatic-ETH-wallet-Balance-Transfer.svg?style=for-the-badge
[license-url]: https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/turazashvili
[product-screenshot]: images/screenshot.png
