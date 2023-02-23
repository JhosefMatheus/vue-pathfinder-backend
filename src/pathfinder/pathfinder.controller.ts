import { Body, Controller, Post, Res, UseGuards, Get, Param, Delete, Put } from "@nestjs/common";
import { CreatePathfinderDto, UpdatePathfinderDto } from "./dto";
import { Response } from "express";
import { PathfinderService } from "./pathfinder.service";
import { AuthGuard } from "@nestjs/passport";
import { IDeletePathfinderParams, IGetPathfinderParams, IGetPathfindersParams, IUpdatePathfinderParams } from "./interface";

@UseGuards(AuthGuard("jwt"))
@Controller("pathfinder")
export class PathfinderController {
    constructor(private readonly pathfinderService: PathfinderService) {}

    @Delete(":pathfinderId")
    async deletePathfinder(@Res() response: Response, @Param() params: IDeletePathfinderParams): Promise<Response> {
        const { pathfinderId } = params;

        const { flag, message } = await this.pathfinderService.deletePathfinder(pathfinderId);

        if (flag) {
            return response.status(200).json({
                message
            });
        }

        return response.status(401).json({
            message
        });
    }
    
    @Post("create")
    async createPathfinder(@Res() response: Response, @Body() createPathfinderDto: CreatePathfinderDto): Promise<Response> {
        const { userId, name } = createPathfinderDto;

        const { flag, message } = await this.pathfinderService.createPathfinder(userId, name);

        if (flag) {
            return response.status(200).json({
                message
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Get("pathfinders/:userId")
    async getUserPathfinders(@Res() response: Response, @Param() params: IGetPathfindersParams): Promise<Response> {
        const { userId } = params;

        const { flag, message, pathfinders } = await this.pathfinderService.getUserPathfinders(userId);

        if (flag) {
            return response.status(200).json({
                message,
                pathfinders
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Get(":userId/:pathfinderId")
    async getPathfinder(@Res() response: Response, @Param() params: IGetPathfinderParams): Promise<Response> {
        const { userId, pathfinderId } = params;

        const { flag, message, currentPathfinder } = await this.pathfinderService.getPathfinder(userId, pathfinderId);

        if (flag) {
            return response.status(200).json({
                message,
                currentPathfinder
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Put(":userId/:pathfinderId")
    async updatePathfinder(@Res() response: Response, @Param() params: IUpdatePathfinderParams, @Body() updatePathfinderDto: UpdatePathfinderDto): Promise<Response> {
        const { userId, pathfinderId } = params;
        const { name } = updatePathfinderDto;

        const { flag, message } = await this.pathfinderService.updatePathfinder(userId, pathfinderId, name);

        if (flag) {
            return response.status(200).json({
                message
            });
        }

        return response.status(401).json({
            message
        });
    }
}