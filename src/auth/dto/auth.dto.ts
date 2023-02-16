import { IsString, IsNotEmpty } from "class-validator";

export class SignInDto {
    @IsString()
    @IsNotEmpty()
    login: string;

    @IsString()
    @IsNotEmpty()
    password: string;
}

export class SignUpDto {
    @IsString()
    @IsNotEmpty()
    fullName: string;

    @IsString()
    @IsNotEmpty()
    login: string;

    @IsString()
    @IsNotEmpty()
    password: string;
}