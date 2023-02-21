import { Injectable } from "@nestjs/common";
import { ConfigService } from "@nestjs/config";
import { JwtService } from "@nestjs/jwt";
import { ITokenVerify } from "./interface";

@Injectable()
export class TokenService {
    constructor(private readonly jwtService: JwtService, private readonly configService: ConfigService) {}

    async tokenVerify(token: string): Promise<ITokenVerify> {
        const tokenOptions = {
            secret: this.configService.get("JWT_SECRET"),
            algorithm: "HS256"
        }

        try {
            const tokenVerify = await this.jwtService.verifyAsync(token, tokenOptions);

            return {
                flag: true,
                message: "Token válido.",
                tokenVerify
            }
        } catch (error) {
            return {
                flag: false,
                message: "Token inválido."
            }
        }
    }
}