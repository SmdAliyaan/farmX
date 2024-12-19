const express = require('express');
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

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
