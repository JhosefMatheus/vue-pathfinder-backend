import { Pathfinder } from "@prisma/client";

export interface ICreatePathfinder {
    flag: boolean;
    message: string;
}

export interface IGetPathfindersParams {
    userId: string;
}

export interface IGetUserPathfinders {
    flag: boolean;
    message: string;
    pathfinders?: Pathfinder[]
}

export interface IDeletePathfinderParams {
    pathfinderId: string;
}

export interface IDeletePathfinder {
    flag: boolean;
    message: string;
}

export interface IGetPathfinderParams {
    userId: string;
    pathfinderId: string;
}

export interface IGetPathfinder {
    flag: boolean;
    message: string;
    currentPathfinder?: Pathfinder;
}

export interface IUpdatePathfinderParams {
    userId: string;
    pathfinderId: string;
}