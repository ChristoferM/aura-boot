public List<Usuario> buscarDatos() {
		String sql = "SELECT * FROM public.usuario";
		return jdbcTemplate.query(sql, new UsuarioRowMapper());
        } 
public class UsuarioRowMapper implements RowMapper<Usuario> {

		@Override
		public Usuario mapRow(ResultSet rs, int rowNum) throws SQLException {
			Usuario usuario = new Usuario();
            
              usuario.setNombre(rs.getString("nombre"));
              usuario.setApellido(rs.getString("apellido"));
              usuario.setEdad(rs.getInteger("edad"));
              usuario.setCorre(rs.getString("corre"));
              usuario.setConstrasenna(rs.getString("constrasenna"));
			return usuario;
		}
	}
    