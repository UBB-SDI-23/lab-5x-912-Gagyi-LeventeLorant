import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";
import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Film } from "../../models/Film";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
export const FilmActorPayStatistics = () => {
	const [loading, setLoading] = useState(false);
	const [films, setFilms] = useState<Film[]>([]);

	useEffect(() => {
		setLoading(true);
		fetch(`${BACKEND_API_URL}/films/film_by_actor_payment_list/`)
			.then((response) => response.json())
			.then((data) => {
				setFilms(data);
				setLoading(false);
			});
	}, []);

	return (
		<Container>
			<h1>Films Ordered By Average Actor Payment</h1>

			{loading && <CircularProgress />}
			{!loading && films.length === 0 && <p>No films found</p>}
			{!loading && films.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>#</TableCell>
								<TableCell align="right">Film Name</TableCell>
								<TableCell align="center">Rating</TableCell>
                        <TableCell align="center">Average Actor Payment</TableCell>
								
							</TableRow>
						</TableHead>
						<TableBody>
							{films.map((film, index) => (
								<TableRow key={film.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
									<TableCell component="th" scope="row">
											{film.name}
									</TableCell>
									<TableCell align="center">{film.rating}</TableCell>
                           <TableCell align="center">{film.average_pay}</TableCell>
									
									
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	);
};