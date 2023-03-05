import { Controller, Get, UseGuards, Res, Param } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { Response } from "express";
import { ClassService } from "./class.service";
import { IGetClassDataParams, IGetClassPathfinderProgressParams } from "./interface";

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

    @Get("progress/:pathfinderId/:classId")
    async getClassPathfinderProgress(@Res() response: Response, @Param() params: IGetClassPathfinderProgressParams): Promise<Response> {
        const { pathfinderId, classId } = params;

        const pathfinderProgress = await this.classService.getClassPathfinderProgress(pathfinderId, classId);

        return response.status(200).json({
            pathfinderProgress
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