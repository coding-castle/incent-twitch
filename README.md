# Twitch Incent Farmer

You need Node.js and npm/yarn

Run either `npm i` or `yarn` to install dependencies

Go to `https://my.incent.com` and log in to your account. Open the DevTools and inspect the Network requests to find your JWT token. Refresh the page with the DevTools open, find any authenticated request like "current_user" and grab the JWT token (starting with "ey") and put it into a `.env` file.

Now run `yarn build` / `npm run build` and `yarn start` / `npm run start` to start listening to Twitch Chat for tokens.

If a message with the format "AGURIN-XXXXX" is found the bot will try to redeem that code with your JWT.

Only works for Agurins channel atm. I might extend it later to work with more channels.
