import { Class } from "@prisma/client";
import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { IGetClasses } from "./dto";

@Injectable()
export class ClassService {
    constructor(private readonly prismaService: PrismaService) {}

    async getClasses(): Promise<IGetClasses> {
        const classes: Class[] = await this.prismaService.class.findMany();

        return {
            classes
        }
    }
}