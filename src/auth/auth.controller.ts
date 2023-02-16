import { Controller, Post, Res, Body } from "@nestjs/common";
import { Response } from "express";
import { AuthService } from "./auth.service";
import { SignInDto } from "./dto";

@Controller("auth")
export class AuthController {
    constructor(private readonly authService: AuthService) {}

    @Post("signIn")
    async signIn(@Res() response: Response, @Body() signInDto: SignInDto): Promise<Response> {
        const { login, password } = signInDto;

        const { flag, message, token } = await this.authService.signIn(login, password);

        if (flag) {
            return response.status(200).json({
                message,
                token
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Post("signUp")
    async signUp() {}
}