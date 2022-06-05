<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.


Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [Web3](https://pypi.org/project/web3/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Copy or download the repository to your local machine.

### Prerequisites


* Web3
  ```sh
  pip install web3
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/turazashvili/Automatic-ETH-wallet-Balance-Transfer.git
   ```
3. Install Python
   Choose latest release for your OS https://www.python.org/downloads/
4. Enter your Wallets and Key in `loop.py`
   ```py
   private_key = "<Your_Private_Key"
   pub_key ="<Your_wallet>"
   recipient_pub_key = "<Recipient_wallet>"
   ```
5. Enter your gasPrice, gasLimit and chainId in `loop.py`
   ```py
    gasPrice = w3.toWei('30', 'gwei')
    gasLimit = 21000
    
    tx = {
            'chainId': 3,
   ```
   You can find your chain ID here: https://chainlist.wtf/
   Your current required gasPrice in gwei here: 
     * [Ethereum](https://etherscan.io/gastracker)
     * [Polygon](https://polygonscan.com/gastracker)
     * [Binance](https://bscscan.com/gastracker)
     * [Avalanche]( https://snowtrace.io/gastracker)

6. Run the script
   ```py
    python loop.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage



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
