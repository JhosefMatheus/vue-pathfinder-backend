import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { ISignIn, ISignUp } from "./interface";
import { Prisma, User } from "@prisma/client";
import * as argon2 from "argon2";
import { JwtService } from "@nestjs/jwt";
import { ConfigService } from "@nestjs/config";

@Injectable()
export class AuthService {
    constructor(private readonly prismaService: PrismaService, private readonly jwtService: JwtService, private readonly configService: ConfigService) {}

    private async generateToken(user: User): Promise<string> {
        const jwtPayload = {
            sub: user.id,
            username: user.fullName,
            login: user.login
        };

        const jwtOptions = {
            secret: this.configService.get("JWT_SECRET"),
            expiresIn: "2d"
        }

        const jwtToken: string = await this.jwtService.signAsync(jwtPayload, jwtOptions);

        return jwtToken;
    }

    async signIn(login: string, password: string): Promise<ISignIn> {
        try {
            const user = await this.prismaService.user.findFirstOrThrow({
                where: {
                    login: {
                        equals: login
                    }
                }
            });

            const passwordVerify: boolean = await argon2.verify(user.password, password);

            if (passwordVerify) {
                const jwtToken: string = await this.generateToken(user);

                return {
                    flag: true,
                    message: "Usuário logado com sucesso.",
                    token: jwtToken
                }
            }

            return {
                flag: false,
                message: "Login ou senha inválidos."
            }

        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Login ou senha inválidos."
                    }
                }
            }
        }
    }

    async signUp(fullName: string, login: string, password: string): Promise<ISignUp> {
        try {
            const hashedPassword: string = await argon2.hash(password);

            await this.prismaService.user.create({
                data: {
                    fullName: fullName,
                    login: login,
                    password: hashedPassword
                }
            });

            return {
                flag: true,
                message: "Usuário cadastrado com sucesso."
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2002") {
                    return {
                        flag: false,
                        message: `Login ${login} já está sendo utilizado, por favor forneça outro login.`
                    }
                }
            }
        }
    }
}