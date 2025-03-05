import { Request, Response } from 'express';

export const getHome = (req: Request, res: Response) => {
    res.send('Welcome to the Express App!');
};

export const getAbout = (req: Request, res: Response) => {
    res.send('About this application');
};