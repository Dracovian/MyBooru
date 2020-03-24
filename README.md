# MyBooru
Generate an image booru from scraped data.

## What is MyBooru
MyBooru is my attempt at fixing a major issue with scraping multimedia... organization.

Boorus, when done correctly, are near-perfect examples of mass media organization.

So the concept is as follows:

1. Run a simple web server using sockets in one of three modes:
	- Offline(localhost  ): The server can only be accessed via the [loopback address](http://127.0.0.1/)
	- Closed (LAN network): The server can only be accessed from within the same local network.
	- Online (Internet   ): The server can be accessed remotely from anywhere in the world via a secure tunnel address.
2. Interface with a module framework made specifically for integrating with MyBooru.
	- The module framework will work in the backend.
	- The MyBooru contents will work in the frontend.
	- The backend will also dictate how scraper scripts will be written while providing useful functions.
3. The scripts will be called from the frontend.
	- Creating a new tag will prompt the scripts to begin grabbing data from their respective target sources.
	- The scripts will also detect the other tags associated with the grabbed images and push them as suggestions.
		- Suggested tags aren't applied automatically, they have to be approved by the booru manager.
4. The frontend will also provide a means of theme creation.
	- The physical layout of the booru will mainly remain unchanged.
	- The themes will only require some stylesheets.
	- The backend is responsible for recognizing new themes and adding them to the list of available themes.
5. The backend will put itself inbetween all communications with the database.
	- All inputs will be sanitized by default.
	- All database statements will be prepared before execution.
6. There will be some SEO in the form of simple unmasked redirects.
	- **HTTP 301** will be used for most of the SEO redirects.
	- **HTTP 302** will be used for most redirects from areas that are unfinished.
		
## Screenshots
*(Coming Soon)*

## Feature Checklist
More features will be added as the project progresses.

- [ ] HTTP Server
	- [ ] Access and Error Logs
	- [ ] Secure Tunnelling
	- [ ] SEO-Friendly Redirects
	- [ ] Concurrent Connections
	- [ ] Secure Headers
		- [ ] Cross-Origin Resource Sharing
		- [ ] Content Security Policy
		- [ ] Strict Transport Security
		- [ ] Referrer Policy
		- [ ] Feature Policy
		- [ ] X-Frame Options
		- [ ] X-Content Type Options
		- [ ] X-XSS Protection
	- [ ] Identifier Headers
		- [ ] Server
		- [ ] Host
		- [ ] Origin
		- [ ] Referer
		- [ ] Content-Type
		- [ ] Accepted-Encoding
		- [ ] Cookies
- [ ] Booru Framework
	- [ ] Theming System
	- [ ] Templating System
	- [ ] Responsive Design
	- [ ] CBZ/CBR/CB7 Viewer
	- [ ] Image Viewer
	- [ ] Video Player
	- [ ] Flash to HTML5 Canvas Conversion
- [ ] Module Framework
	- [ ] API Generation
	- [ ] Exif Remover
	- [ ] Media Compressor
		- [ ] PNG Compression
		- [ ] VP9 Compression
		- [ ] SWF Compression
	- [ ] CBZ/CBR/CB7 Support
	- [ ] Mimetype Filtering
	- [ ] asyncio
	- [ ] aiohttp
	- [ ] Database Management
		- [ ] SQLite
		- [ ] MariaDB/MySQL
		- [ ] MongoDB
		- [ ] Redis
		- [ ] PostgreSQL
		- [ ] ODBC
	- [ ] Account Management
		- [ ] Usergroups and Permissions System
		- [ ] Account Creation
	- [ ] Community Management
		- [ ] Inline Moderation
		- [ ] Secure Admin Control Panel
		- [ ] Account Quality and Trust System
		- [ ] Automated Tasking
	- [x] Cryptography
		- [x] Scrypt Password Hashing
			- [x] Random Salt Generation
			- [x] Custom Hash Layout