import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { ISignIn } from "./interface";
import { Prisma } from "@prisma/client";

@Injectable()
export class AuthService {
    constructor(private readonly prismaService: PrismaService) {}

    async signIn(login: string, password: string): Promise<ISignIn> {
        try {
            const user = await this.prismaService.user.findFirstOrThrow({
                where: {
                    login: {
                        equals: login
                    },
                    password: {
                        equals: password
                    }
                }
            });

            return {
                flag: true,
                message: "Usuário logado com sucesso.",
                token: "token"
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

    async signUp() {}
}