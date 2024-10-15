// Inicialización de la escena, cámara y renderizador
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('molecule-viewer').appendChild(renderer.domElement); // Ajuste aquí

// Agregar luz a la escena
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0xffffff, 1);
pointLight.position.set(10, 10, 10);
scene.add(pointLight);

// Función para crear una esfera que representa un átomo
function createAtom(radius, color) {
    const geometry = new THREE.SphereGeometry(radius, 32, 32);
    const material = new THREE.MeshPhongMaterial({ color: color });
    const sphere = new THREE.Mesh(geometry, material);
    return sphere;
}

// Ejemplo de molécula: Agua (H2O)
function createWaterMolecule() {
    const oxygen = createAtom(0.5, 0xff0000); // Oxígeno en rojo
    const hydrogen1 = createAtom(0.3, 0x0000ff); // Hidrógeno en azul
    const hydrogen2 = createAtom(0.3, 0x0000ff); // Hidrógeno en azul

    // Posicionar los átomos
    oxygen.position.set(0, 0, 0);
    hydrogen1.position.set(1, 0, 0); // Primer hidrógeno
    hydrogen2.position.set(-1, 0, 0); // Segundo hidrógeno

    // Agregar átomos a la escena
    scene.add(oxygen);
    scene.add(hydrogen1);
    scene.add(hydrogen2);
}

// Crear la molécula de agua
createWaterMolecule();

// Posicionar la cámara
camera.position.z = 5;

// Función de animación
function animate() {
    requestAnimationFrame(animate);

    // Rotar la escena para una mejor visualización
    scene.rotation.y += 0.01;

    renderer.render(scene, camera);
}

// Manejar el redimensionamiento de la ventana
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Iniciar la animación
animate();