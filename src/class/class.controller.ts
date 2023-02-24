import { Controller, Get, UseGuards, Res, Param } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { Response } from "express";
import { ClassService } from "./class.service";
import { IGetClassDataParams } from "./interface/class.interface";

@UseGuards(AuthGuard("jwt"))
@Controller("class")
export class ClassController {
    constructor(private readonly classService: ClassService) {}

    @Get("classes")
    async getClasses(@Res() response: Response): Promise<Response> {
        const { classes } = await this.classService.getClasses();

        return response.status(200).json({
            classes
        });
    }

    @Get(":id")
    async getClassData(@Res() response: Response, @Param() params: IGetClassDataParams): Promise<Response> {
        const { id } = params;

        const { flag, message, currentClass } = await this.classService.getClassData(id);

        if (flag) {
            return response.status(200).json({
                message,
                currentClass
            });
        }

        return response.status(401).json({
            message
        });
    }
}