import dotenv from "dotenv"
dotenv.config()

export const JWT = process.env.JWT || ""

export const API_URL = "https://api.incent.com/v1"
