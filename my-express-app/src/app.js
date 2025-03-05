import express from 'express';

import bodyParser from 'body-parser';
import routes from './routes/index.js';
import tableRoutes from './routes/table.js';

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use('/api', routes);
app.use('/tables', tableRoutes); // Add this line to include table routes

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});