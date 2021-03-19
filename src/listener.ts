import { Client } from "tmi.js"
import { redeem } from "./api"
import logger from "./logger"

export async function listen() {
    const client = new Client({
        connection: { secure: true, reconnect: true },
        channels: ["agurin"],
    })

    client.connect()

    client.on("message", async (channel, _, message) => {
        logger.info(`${channel} ${message}`)
        if (message.includes("AGURIN-")) {
            const splits = message.split(" ")
            const found = splits.find((s) => s.includes("AGURIN-"))
            const result = found?.substring(0, 12)
            if (result) {
                await redeem(result)
            }
        }
    })
}
