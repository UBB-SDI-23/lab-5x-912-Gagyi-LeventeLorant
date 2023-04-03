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
	Toolbar,
	Button,
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

export const AllFilms = () => {
	const [loading, setLoading] = useState(false);
	const [films, setFilms] = useState<Film[]>([]);

	useEffect(() => {
		setLoading(true);
		fetch(`${BACKEND_API_URL}/films/`)
			.then((response) => response.json())
			.then((data) => {
				setFilms(data);
				setLoading(false);
			});
	}, []);

	const orderByRating=()=>{
		const sorted = [...films].sort((a, b) => b.rating - a.rating);
		setFilms(sorted);
	}


	return (
		<Container>
			<h1>All films</h1>

			{loading && <CircularProgress />}
			{!loading && films.length === 0 && <p>No films found</p>}
			{!loading && (
				<Toolbar>
				<IconButton component={Link} sx={{ mr: 3 }} to={`/films/add`}>
					<Tooltip title="Add a new film" arrow>
						<AddIcon color="primary" />
					</Tooltip>
				</IconButton>
				<Button
						onClick={orderByRating}
						// component={Link}
						// color="inherit"
						// sx={{ mr: 5 }}
						// startIcon={<LocalLibraryIcon />}
						>Order By Rating
					</Button>
					</Toolbar>
			)}
			{!loading && films.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>#</TableCell>
								<TableCell align="right">Name</TableCell>
								<TableCell align="right">Release Date</TableCell>
								<TableCell align="right">Rating</TableCell>
								<TableCell align="center">Operations</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							{films.map((film, index) => (
								<TableRow key={film.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/films/${film.id}/details`} title="View film details">
											{film.name}
										</Link>
									</TableCell>
									<TableCell align="right">{film.release_date}</TableCell>
									<TableCell align="right">{film.rating}</TableCell>
									<TableCell align="right">
										<IconButton
											component={Link}
											sx={{ mr: 3 }}
											to={`/films/${film.id}/details`}>
											<Tooltip title="View film details" arrow>
												<ReadMoreIcon color="primary" />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/films/${film.id}/edit`}>
											<EditIcon />
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/films/${film.id}/delete`}>
											<DeleteForeverIcon sx={{ color: "red" }} />
										</IconButton>
									</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	);
};