import java.util.List;

import org.springframework.data.repository.CrudRepository;

public interface GoldMedalsRepository extends CrudRepository<GoldMedal, Long> {
    List<GoldMedal> findAllOrderByYear(Boolean order);
    List<GoldMedal> findAllOrderBySeason(Boolean order);
    List<GoldMedal> findAllOrderByCity(Boolean order);
    List<GoldMedal> findAllOrderByName(Boolean order);
    List<GoldMedal> findAllOrderByEvent(Boolean order);

}