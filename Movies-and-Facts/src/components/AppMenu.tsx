import { Box, AppBar, Toolbar, IconButton, Typography, Button } from "@mui/material";
import { Link, useLocation } from "react-router-dom";
import SchoolIcon from "@mui/icons-material/School";
import LocalLibraryIcon from "@mui/icons-material/LocalLibrary";
import ArticleIcon from '@mui/icons-material/Article';
import MovieIcon from '@mui/icons-material/Movie';
import VideocamIcon from '@mui/icons-material/Videocam';
import PeopleAltIcon from '@mui/icons-material/PeopleAlt';
import MenuIcon from '@mui/icons-material/Menu';

export const AppMenu = () => {
	const location = useLocation();
	const path = location.pathname;

	return (
		<Box  sx={{ flexGrow: 1 }}>
			<AppBar  position="static" sx={{ marginBottom: "20px" }}>
				<Toolbar className="toolbar">
					<IconButton
						className="toolIcon"
						component={Link}
						to="/"
						size="large"
						edge="start"
						color="inherit"
						aria-label="school"
						sx={{ mr: 2 }}>
						<MenuIcon />
					</IconButton>
					<Typography variant="h6" component="div" sx={{ mr: 5 }}>
						Movies & facts
					</Typography>
					<Button
						className="toolIcon"
						variant={path.startsWith("/films") ? "outlined" : "text"}
						to="/films/?page=1"
						component={Link}
						color="inherit"
						sx={{ mr: 5 }}
						startIcon={<MovieIcon />}>
						Films
					</Button>
					<Button
						className="toolIcon"
						variant={path.startsWith("/screenings") ? "outlined" : "text"}
						to="/screenings/?page=1"
						component={Link}
						color="inherit"
						sx={{ mr: 5 }}
						startIcon={<VideocamIcon />}>
						Screenings
					</Button>
					<Button
						className="toolIcon"
						variant={path.startsWith("/actors") ? "outlined" : "text"}
						to="/actors/?page=1"
						component={Link}
						color="inherit"
						sx={{ mr: 5 }}
						startIcon={<PeopleAltIcon />}>
						Actors
					</Button>
					<Button
						className="toolIcon"
						variant={path.startsWith("/statistics") ? "outlined" : "text"}
						to="/statistics"
						component={Link}
						color="inherit"
						sx={{ mr: 5 }}
						startIcon={<ArticleIcon />}>
						Statistics
					</Button>
				</Toolbar>
			</AppBar>
		</Box>
	);
};