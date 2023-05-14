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
import { Actor } from "../../models/Actor";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';

export const AllActors = () => {
	const [loading, setLoading] = useState(false);
	const [actors, setActors] = useState<Actor[]>([]);
    const [currentPage, setCurrentPage] = useState(1);
    const totalPages = Math.ceil(1000000 / 10);

	useEffect(() => {
		setLoading(true);
		fetch(`${BACKEND_API_URL}/actors/?page=${currentPage}`)
			.then((response) => response.json())
			.then((data) => {
				setActors(data);
				setLoading(false);
			});
	}, []);

	const handleNextPage = () => {
		if (currentPage < totalPages) {
		  
		  setCurrentPage(currentPage + 1);
		  console.log(currentPage);
		  setLoading(true);
		  fetch(`${BACKEND_API_URL}/actors/?page=${currentPage}`)
		  .then((response) => response.json())
		  .then((data) => {
			setActors(data);
			setLoading(false);
		  });
		  
		}
	  };

	  const handlePrevPage = () => {
		if (currentPage > 1) {
		  
		  setCurrentPage(currentPage - 1);
		  console.log(currentPage);
		  setLoading(true);
		  fetch(`${BACKEND_API_URL}/actors/?page=${currentPage}`)
		  .then((response) => response.json())
		  .then((data) => {
			setActors(data);
			setLoading(false);
		  });
		   
		}
	  };


	return (
		<Container>
			<h1>All actors</h1>

			{loading && <CircularProgress />}
			{!loading && actors.length === 0 && <p>No actors found</p>}
			{!loading && (
				<Toolbar>
					<IconButton onClick={handlePrevPage} style={{ marginRight:'370px'}} component={Link} sx={{ mr: 3 }} to={`/actors/?p=${currentPage}`} disabled={currentPage === 1}>
					<Tooltip title="Previous">
					<ArrowBackIosIcon sx={{ color: "white" }} />
					</Tooltip>
				</IconButton>
				<IconButton component={Link} sx={{ mr: 3 }} to={`/actors/add`}>
					<Tooltip title="Add a new actor" arrow>
						<AddIcon color="primary" />
					</Tooltip>
				</IconButton>
					<IconButton style={{ marginLeft:'370px'}} onClick={handleNextPage} component={Link} sx={{ mr: 3 }}  to={`/actors/?p=${currentPage}`} disabled={currentPage === totalPages}>
            		<Tooltip title="Next">
             		<ArrowForwardIosIcon sx={{ color: "white" }} />
            		</Tooltip>
          			</IconButton>
					</Toolbar>
			)}
			{!loading && actors.length > 0 && (
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
							{actors.map((actor, index) => (
								<TableRow key={actor.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/actors/${actor.id}/details`} title="View actor details">
											{actor.name}
										</Link>
									</TableCell>
									<TableCell align="right">{actor.birth_date}</TableCell>
									<TableCell align="right">{actor.height}</TableCell>
									<TableCell align="right">
										<IconButton
											component={Link}
											sx={{ mr: 3 }}
											to={`/actors/${actor.id}/details`}>
											<Tooltip title="View actor details" arrow>
												<ReadMoreIcon color="primary" />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/actors/${actor.id}/edit`}>
											<EditIcon />
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/actors/${actor.id}/delete`}>
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