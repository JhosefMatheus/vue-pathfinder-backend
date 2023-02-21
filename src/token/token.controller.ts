import { Controller, Get, Res, Headers } from "@nestjs/common";
import { Response } from "express";
import { TokenDto } from "./dto";
import { TokenService } from "./token.service";

@Controller("token")
export class TokenController {
    constructor(private readonly tokenServie: TokenService) {}

    @Get("verify")
    async tokenVerify(@Res() response: Response, @Headers() headers: TokenDto): Promise<Response> {
        const token = headers.authorization.replace("Bearer ", "");

        const { flag, message, tokenVerify } = await this.tokenServie.tokenVerify(token);

        if (flag) {
            return response.status(200).json({
                message,
                tokenData: tokenVerify
            });
        }

        return response.status(401).json({
            message
        });
    }
}