import java.util.List;

import org.springframework.data.repository.CrudRepository;

public interface CountryRepository extends CrudRepository<Country, Long> {
    List<Country> findAllOrderByName(Boolean order);
    List<Country> findAllOrderByGpd(Boolean order);
    List<Country> findAllOrderByPopulation(Boolean order);
    List<Country> findAllOrderByMedals(Boolean order);
}