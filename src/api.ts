import axios from "axios"
import { API_URL, JWT } from "./config"
import logger from "./logger"

axios.defaults.headers.common["Authorization"] = `Bearer ${JWT}`

export async function redeem(code: string) {
    try {
        const { data } = await axios.post(
            `${API_URL}/organisations/campaigns/unicodes/apply_code`,
            { code },
        )
        if (data.status === "Accepted") {
            logger.info("\n\nSuccessfully redeemed code 🎉\n\n")
        }
    } catch (error) {
        logger.error("\n\nSomething went wrong redeeming a code 🛑\n\n")
    }
}
