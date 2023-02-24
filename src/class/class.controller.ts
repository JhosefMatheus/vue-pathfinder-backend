import { Controller, Get, UseGuards, Res } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { Response } from "express";
import { ClassService } from "./class.service";

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
}