import { Class } from "@prisma/client";

export interface IGetClassDataParams {
    id: string;
}

export interface IGetClassData {
    flag: boolean;
    message: string;
    currentClass?: Class;
}