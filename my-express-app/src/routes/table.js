import express from 'express';

const router = express.Router();

// Route for creating a new reservation
router.post('/reservations', (req, res) => {
    const { numberOfPeople, time, date } = req.body;

    // Validate numberOfPeople
    if (numberOfPeople < 1 || numberOfPeople > 6) {
      return res.status(400).send('Number of people must be between 1 and 6');
    }

    // Validate time
    const validTimes = ['17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00'];
    if (!validTimes.includes(time)) {
      return res.status(400).send('Time must be between 5:00 PM and 11:00 PM in 30-minute intervals');
    }

    // Validate date
    const currentDate = new Date();
    const reservationDate = new Date(date);
    if (reservationDate < currentDate.setHours(0, 0, 0, 0)) {
      return res.status(400).send('Date must be today or in the future');
    }
    // Logic to create a new reservation
    res.status(201).send('Reservation created successfully');
});

// Route for deleting (cancelling) an existing reservation
router.delete('/reservations/:id', (req, res) => {
    const { id } = req.params;
    // Logic to delete an existing reservation
    res.status(200).send(`Reservation with id ${id} cancelled successfully`);
});

export default router;