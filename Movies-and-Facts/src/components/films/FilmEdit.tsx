import { Button, Card, CardActions, CardContent, IconButton, TextField } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Film } from "../../models/Film";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";

export const FilmUpdate = () => {
	const navigate = useNavigate();
    const { filmId } = useParams();

	const [film, setFilm] = useState<Film>({
		name: "",
        release_date: "",
        on_netfilx: false,
        profit: 0,
        rating: 0,
        nr_of_screenings: 0
	});

    useEffect(() => {
        const fetchFilm = async () => {
           try {
              // const response = await axios.get(`${BACKEND_API_URL}/departments/${departmentId}`);
              // setDepartment(response.data);
              const response = await fetch(`${BACKEND_API_URL}/films/${filmId}`);
              const film = await response.json();
              setFilm(film);
           } catch (error) {
              console.log(error);
           }
        };
        fetchFilm();
     }, [filmId]);
     



	const updateFilm = async (event: { preventDefault: () => void }) => {
		event.preventDefault();
		try {
			await axios.put(`${BACKEND_API_URL}/films/${filmId}`, film);
			navigate("/films");
		} catch (error) {
			console.log(error);
		}
	};

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/films`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<form onSubmit={updateFilm}>
						<TextField
							id="name"
							label="Name"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
                            value={film.name}
							onChange={(event) => setFilm({ ...film, name: event.target.value })}
						/>
						<TextField
							id="release_date"
							label="Release Date"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
                            value={film.release_date}
							onChange={(event) => setFilm({ ...film, release_date: event.target.value })}
						/>
						<TextField
							id="profit"
							label="Profit"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
                            value={film.profit}
							onChange={(event) => setFilm({ ...film, profit: Number(event.target.value )})}
						/>
						<TextField
							id="rating"
							label="Rating"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
                            value={film.rating}
							onChange={(event) => setFilm({ ...film, rating: Number(event.target.value) })}
						/>
                        <TextField
							id="nr_of_screenings"
							label="Number of Screenings"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
                            value={film.nr_of_screenings}
							onChange={(event) => setFilm({ ...film, nr_of_screenings: Number(event.target.value) })}
						/>

						<Button type="submit">Update Film</Button>
					</form>
				</CardContent>
				<CardActions></CardActions>
			</Card>
		</Container>
	);
};