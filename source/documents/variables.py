
class Variables:

    def __init__(self):
        self.name = "Crear Variables"
        self.selectQuery= """public List<{nameClassUp}> buscarDatos() {{
		String sql = "SELECT * FROM {schema}.{nameClass}";
		return jdbcTemplate.query(sql, new {nameClassUp}RowMapper());
        }}"""

        self.rowMapper = """ 
public class {nameClassUp}RowMapper implements RowMapper<{nameClassUp}> {{

		@Override
		public {nameClassUp} mapRow(ResultSet rs, int rowNum) throws SQLException {{
			{nameClassUp} {nameClass} = new {nameClassUp}();
            {Atributos}
			return {nameClass};
		}}
	}}
    """
        self.atributeRowMapper = "              {nameClass}.set{atributoUp}(rs.get{type}(\"{atributo}\"));"
        