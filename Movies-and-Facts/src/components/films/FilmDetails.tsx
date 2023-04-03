import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Film } from "../../models/Film";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

export const FilmDetails = () => {
	const { filmId } = useParams();
	const [film, setFilm] = useState<Film>();

	useEffect(() => {
		const fetchFilm = async () => {
			// TODO: use axios instead of fetch
			// TODO: handle errors
			// TODO: handle loading state
			const response = await fetch(`${BACKEND_API_URL}${filmId}`);
			const film = await response.json();
			setFilm(film);
		};
		fetchFilm();
	}, [filmId]);

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/films`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<h1>Film Details</h1>
					<p>Film Name: {film?.name}</p>
					<p>Film Profit: {film?.profit}</p>
					<p>Film Rating: {film?.rating}</p>
					<p>Film Release Date: {film?.release_date}</p>
				</CardContent>
				<CardActions>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/films/${filmId}/edit`}>
						<EditIcon />
					</IconButton>

					<IconButton component={Link} sx={{ mr: 3 }} to={`/films/${filmId}/delete`}>
						<DeleteForeverIcon sx={{ color: "red" }} />
					</IconButton>
				</CardActions>
			</Card>
		</Container>
	);
};