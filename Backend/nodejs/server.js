const express = require('express');
const path = require('path');
const app = express();
const connectDB = require('./config/dbConfig');
const cors = require('cors');

// Connect to Database
connectDB();

// Middleware
app.use(cors());
app.use(express.json());

// Import Routes
const authRoutes = require('./routes/authRoutes');

// Route Middlewares
app.use('/api/user', authRoutes);

// Serve static files from the React app
app.use(express.static(path.join(__dirname, '../frontend/public')));

// The "catchall" handler: for any request that doesn't match one above, send back React's index.html file.
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend/public/index.html'));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
