import { Container, Row, Col } from 'react-bootstrap';
import { useState } from 'react';
import { Carousel } from 'react-bootstrap';
import { useTranslation } from 'react-i18next';
import Modal_Component from '../../Component-Modal/Modal-Component';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../../Standard-Component-style.css';
import '../Game.css';

export default function UnderHome_Component(){
    const { t, i18n } = useTranslation("global");

    const [index, setIndex] = useState(0);

    const handleSelect = (selectedIndex) => {
        setIndex(selectedIndex);
    };

    const [modalActive, setModalActive] = useState(false);

    return(
        <div>
            <Container fluid className='fluid-fix'>
                <Row>
                    <Col>
                        <h1 className='mar-72'>{t("game.game-2-h1")}</h1>
                    </Col>
                </Row>
                {/* Слайдер */}
                <Carousel activeIndex={index} onSelect={handleSelect} interval={2000} className='mar-96'>
                    <Carousel.Item>
                        <img className="d-block w-50 mar-auto" src="/img/game-screens/game-2/screen1.png" alt="First slide" />
                    </Carousel.Item>
                    <Carousel.Item>
                        <img className="d-block w-50 mar-auto" src="/img/game-screens/game-2/screen2.png" alt="First slide" />
                    </Carousel.Item>
                    <Carousel.Item>
                        <img className="d-block w-50 mar-auto" src="/img/game-screens/game-2/screen3.png" alt="First slide" />
                    </Carousel.Item>
                </Carousel>
                {/* Кінець слайдеру */}
                <Container>
                    <Row className='container-game mar-48'>
                        <p className='mar-16'>{t("game.game-2-paragraph-1")}</p>
                        <p className='mar-16'>{t("game.game-2-paragraph-2")}</p>
                        <p className='mar-16'>{t("game.game-2-paragraph-3")}</p>
                        <p className='mar-16'>{t("game.game-2-paragraph-4")}</p>
                        <p className='mar-24'>{t("game.game-2-paragraph-5")}</p>
                        {/* <a href="/public/materials/games/Under Home.zip" target="_blank" download="Under Home.zip" className="btn w-25">{t("about.download")}</a> */}
                        <span className="btn w-25" onClick={() => setModalActive(true)}>{t("about.download")}</span>
                    </Row>
                </Container>
            </Container>
            <Modal_Component active={modalActive} setActive={setModalActive} downloadPath={"/public/materials/games/Under Home.zip"} downloadName={"Under Home.zip"}/>
        </div>
    )
}